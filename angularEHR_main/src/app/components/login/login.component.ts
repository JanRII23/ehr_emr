import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  type: string = "password"; //this is actually a built in feature of showing dots when setting as a password
  isText: boolean = false;
  eyeIcon: string = "visibility_off";
  constructor() { }

  ngOnInit(): void {
  }

  hideShowPass(){ //question marks are if logics and ! is opposite and this is refering to the specific instance
      this.isText = !this.isText;
      this.isText ? this.eyeIcon = "visibility" : this.eyeIcon = "visibility_off";
      this.isText ? this.type = "text" : this.type = "password";
  }
}
