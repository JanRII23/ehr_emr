import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-task-manager',
  templateUrl: './task-manager.component.html',
  styleUrls: ['./task-manager.component.scss']
})
export class TaskManagerComponent implements OnInit {

  taskForm !: FormGroup;
  tasks : any [] = [];
  inprogress: any [] = [];
  done: any[] = [];
  constructor(private fb : FormBuilder) { }

  ngOnInit(): void {
    this.taskForm = this.fb.group({
      item : ['', Validators.required]
    })
  }

}
