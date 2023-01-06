import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { NgToastService } from 'ng-angular-popup';
import ValidateForm from 'src/app/helpers/validateForms';
import { AuthService } from 'src/app/services/auth.service';
import { UserStoreService } from 'src/app/services/user-store.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  type: string = "password"; //this is actually a built in feature of showing dots when setting as a password
  isText: boolean = false;
  eyeIcon: string = "visibility_off";
  loginForm! : FormGroup;
  constructor(private fb: FormBuilder, private auth: AuthService, private router: Router, private toast: NgToastService, private userStore: UserStoreService) { }

  ngOnInit(): void {
    this.loginForm = this.fb.group({
      username: ['', Validators.required],
      password:['', Validators.required]
    })
  }

  onLogin(){

    if (this.loginForm.valid){

      this.auth.login(this.loginForm.value)
      .subscribe({
        next:(res)=>{
          // alert(res.message);
          this.loginForm.reset();
          this.auth.storeToken(res.accessToken);
          this.auth.storeRefreshToken(res.refreshToken);
          const tokenPayload = this.auth.decodedToken();
          this.userStore.setFullNameForStore(tokenPayload.name);
          this.userStore.setRoleForStore(tokenPayload.role);
          this.toast.success({detail:"SUCCESS", summary: res.message, duration: 5000});
          this.router.navigate(['todo']);
        },
          error:(err)=>{
            // alert(err?.error.message)
            this.toast.error({detail:"ERROR", summary: "Username or Password is wrong!", duration: 5000});
          }
      })

    }else{
      ValidateForm.validateAllFormFields(this.loginForm);
    }

  }

  hideShowPass(){ //question marks are if logics and ! is opposite and this is refering to the specific instance
      this.isText = !this.isText;
      this.isText ? this.eyeIcon = "visibility" : this.eyeIcon = "visibility_off";
      this.isText ? this.type = "text" : this.type = "password";
  }
}
