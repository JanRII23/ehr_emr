import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Route, Router } from '@angular/router';
import { NgToastService } from 'ng-angular-popup';
import ValidateForm from 'src/app/helpers/validateForms';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  type: string = "password"; //this is actually a built in feature of showing dots when setting as a password
  isText: boolean = false;
  eyeIcon: string = "visibility_off";
  signupForm! : FormGroup
  constructor(private fb: FormBuilder, private auth: AuthService, private router: Router, private toast: NgToastService) { }

  ngOnInit(): void {
    this.signupForm = this.fb.group({
      firstname: ['', Validators.required],
      lastname: ['', Validators.required],
      email: ['', Validators.required],
      username: ['', Validators.required],
      password: ['', Validators.required]
    })
  }


  onSignup(){

    if (this.signupForm.valid){

      this.auth.signUp(this.signupForm.value)
      .subscribe({
        next:(res=>{
          //alert(res.message);
          this.toast.success({detail:"SUCCESS", summary: res.message, duration: 5000});
          this.signupForm.reset();
          this.router.navigate(['login']);
        }),
          error:(err=>{
            // alert(err?.error.message)
            if (err?.error.message == "Username Not Valid!" || err?.error.message == "Email Not Valid!"){
              this.toast.error({detail:"ERROR", summary: err?.error.message, duration: 5000});
            }else{
              alert(err?.error.message)
            }
            
          })
      })

    }else{
      ValidateForm.validateAllFormFields(this.signupForm);
    }

  }



  hideShowPass(){ //question marks are if logics and ! is opposite and this is refering to the specific instance
      this.isText = !this.isText;
      this.isText ? this.eyeIcon = "visibility" : this.eyeIcon = "visibility_off";
      this.isText ? this.type = "text" : this.type = "password";
  }
}


