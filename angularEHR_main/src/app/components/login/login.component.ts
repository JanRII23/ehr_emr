import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import ValidateForm from 'src/app/helpers/validateForms';


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
  constructor(private fb: FormBuilder) { }

  ngOnInit(): void {
    this.loginForm = this.fb.group({
      username: ['', Validators.required],
      password:['', Validators.required]
    })
  }

  onSubmit(){

    if (this.loginForm.valid){

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
