using System.Text;
using System.Text.RegularExpressions;
using angularAuthAPI.Conext;
using angularAuthAPI.Helpers;
using angularAuthAPI.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using Microsoft.IdentityModel.Tokens;
using Microsoft.AspNetCore.Authorization;
using System.Security.Cryptography;
using angularAuthAPI.Models.Dto;

namespace angularAuthAPI.Controllers{

    // controller can be edited more for more ambiguity and either username/email

        [Route("api/[controller]")]
        [ApiController]

        public class UserController : ControllerBase
        {

            private readonly AppDbContext _authContext;

            public UserController(AppDbContext appDbContext)
            {
                _authContext = appDbContext;
                
            }

            [HttpPost("authenticate")]

            public async Task<IActionResult> Authenticate([FromBody] User userObj)
            {
                if (userObj == null){
                    return BadRequest();
                }

                var user = await _authContext.Users.FirstOrDefaultAsync(x => x.Username == userObj.Username);

                if (user == null){
                    return NotFound(new{Message = "Username or Password Wrong!"});
                }

                if (!PasswordHasher.VerifyPassword(userObj.Password, user.Password)){
                    return NotFound(new{Message = "Password Incorrect!"});
                }

                user.Token = CreateJwt(user);

                var newAccessToken = user.Token;
                var newRefreshToken = CreateRefreshToken();
                user.RefreshToken = newRefreshToken;
                user.RefreshTokenExpiryTime = DateTime.UtcNow.AddDays(5);
                await _authContext.SaveChangesAsync();

                return Ok(new TokenApiDto() 
                {
                    // Token = user.Token,
                    // Message = "Login Success!"
                    AccessToken = newAccessToken,
                    RefreshToken = newRefreshToken
                });
            }

            [HttpPost("register")]

            public async Task<IActionResult> RegisterUser([FromBody] User userObj)
            {
                if (userObj == null){
                    return BadRequest();
                }

                //check username
                if (await CheckUserNameExistAsync(userObj.Username)){
                    return BadRequest(new{Message = "Username Not Valid!"});
                   
                }

                //check email
                 if (await CheckEmailExistAsync(userObj.Email)){
                    return BadRequest(new{Message = "Email Not Valid!"});
                    
                }

                //check strength of password
                var pass = CheckPasswordStrength(userObj.Password);
                if (!string.IsNullOrEmpty(pass)){
                    return BadRequest(new {Message = pass.ToString()});
                }

                userObj.Password = PasswordHasher.HashPassword(userObj.Password);
                userObj.Role = "User";
                userObj.Token = "";
                await _authContext.Users.AddAsync(userObj);
                await _authContext.SaveChangesAsync();
                return Ok(new{Message = "User Registered!"});
            }

            private Task<bool> CheckUserNameExistAsync(string username) 
                => _authContext.Users.AnyAsync(x => x.Username == username);
            

            private Task<bool> CheckEmailExistAsync(string email)
                => _authContext.Users.AnyAsync(x => x.Email == email);

            private string CheckPasswordStrength(string password){
                StringBuilder sb = new StringBuilder();
                if(password.Length < 8){
                    sb.Append("Minimum password length should be 8" + Environment.NewLine);
                }

                if (!(Regex.IsMatch(password, "[a-z]") && Regex.IsMatch(password, "[A-Z]") && Regex.IsMatch(password, "[0-9]"))){
                    sb.Append("Password should be Alphanumeric" + Environment.NewLine);
                }

                if (!(Regex.IsMatch(password, "[<,>,@,!,#,$,%,^,&,*,(,),_,+,\\[,\\], {, }, ?, :, ;, |, ', \\, ., /, ~, `, -, =]"))){
                    sb.Append("Password should contain special character" + Environment.NewLine);
                }

                return sb.ToString();
            }

            private string CreateJwt (User user)
            {
                var jwtTokenHandler = new JwtSecurityTokenHandler();
                var key = Encoding.ASCII.GetBytes("veryverysecret.....");
                var identity = new ClaimsIdentity(new Claim[]
                {
                    new Claim(ClaimTypes.Role, user.Role),
                    // new Claim(ClaimTypes.Name, $"{user.FirstName} {user.Lastname}")
                    new Claim(ClaimTypes.Name, $"{user.Username}")
                });

                var credentials = new SigningCredentials(new SymmetricSecurityKey(key), SecurityAlgorithms.HmacSha256);

                var tokenDescriptor = new SecurityTokenDescriptor{
                    Subject = identity,
                    Expires = DateTime.UtcNow.AddSeconds(10),
                    SigningCredentials = credentials
                };

            
                var token = jwtTokenHandler.CreateToken(tokenDescriptor);
                return jwtTokenHandler.WriteToken(token);
            }

            private string CreateRefreshToken()
            {
                var tokenBytes = RandomNumberGenerator.GetBytes(64);
                var refreshToken =Convert.ToBase64String(tokenBytes);

                var tokenInUser = _authContext.Users
                    .Any(a => a.RefreshToken == refreshToken);

                if(tokenInUser){
                    return CreateRefreshToken();
                }
                return refreshToken;
            }

            private ClaimsPrincipal GetPrincipalFromExpiredToken (string token){
                var key = Encoding.ASCII.GetBytes("veryverysecret.....");
                var tokenValidationsParameters = new TokenValidationParameters
                {
                    ValidateAudience = false,
                    ValidateIssuer = false,
                    ValidateIssuerSigningKey = true,
                    IssuerSigningKey = new SymmetricSecurityKey(key),
                    ValidateLifetime = false
                };

                var tokenHandler = new JwtSecurityTokenHandler();
                SecurityToken securityToken;
                var principal = tokenHandler.ValidateToken(token, tokenValidationsParameters, out securityToken);

                var jwtSecurityToken = securityToken as JwtSecurityToken;
                if (jwtSecurityToken == null || !jwtSecurityToken.Header.Alg.Equals(SecurityAlgorithms.HmacSha256, StringComparison.InvariantCultureIgnoreCase)){
                    throw new SecurityTokenException("This is Invalid Token");
                }
                return principal;

            }

            [Authorize]
            [HttpGet]

            public async Task<ActionResult<User>> GetAllUser()
            {
                return Ok(await _authContext.Users.ToListAsync());
            }

            [HttpPost("refresh")]

            public async Task<IActionResult> Refresh(TokenApiDto tokenApiDto){
                if(tokenApiDto is null){
                    return BadRequest("Invalid Client Request");

                }
                string accessToken = tokenApiDto.AccessToken;
                string refreshToken = tokenApiDto.RefreshToken;

                var principal = GetPrincipalFromExpiredToken(accessToken);
                var username = principal.Identity.Name;
                var user = await _authContext.Users.FirstOrDefaultAsync(u => u.Username == username);
                if (user is null || user.RefreshToken != refreshToken || user.RefreshTokenExpiryTime <= DateTime.UtcNow){
                    return BadRequest("Invalid Request");
                }

                var newAccessToken = CreateJwt(user);
                var newRefreshToken = CreateRefreshToken();
                user.RefreshToken = newRefreshToken;
   
                await _authContext.SaveChangesAsync();
                return Ok(new TokenApiDto(){
                    AccessToken = newAccessToken,
                    RefreshToken = newRefreshToken,
                });
            }

        }

}