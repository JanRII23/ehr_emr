import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import ValidateForm from 'src/app/helpers/validateForms';

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
  constructor(private fb: FormBuilder) { }

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


