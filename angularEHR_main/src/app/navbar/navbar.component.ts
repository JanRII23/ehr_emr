import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {

  public users: any = [];
  constructor(private auth: AuthService, private api : ApiService) { }

  ngOnInit() {
    // this.api.getUsers()
    // .subscribe(res=>{
    //   this.users = res;
    // })
  }
  
  logout(){
    this.auth.signOut();
  }

}
