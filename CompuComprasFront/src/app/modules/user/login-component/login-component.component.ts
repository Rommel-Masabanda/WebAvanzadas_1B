import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { UserService } from '../../../services/user.service';
import { loginDTO } from '../../../models/login/loginDTO';
import { Router, RouterLink } from '@angular/router';


@Component({
  selector: 'app-login-component',
  standalone: true,
  imports: [ReactiveFormsModule, RouterLink],
  templateUrl: './login-component.component.html',
  styleUrl: './login-component.component.css'
})
export class LoginComponentComponent {

  
  constructor(private userService:UserService, private router: Router) { }
  readonly loginForm: FormGroup = new FormGroup({
    usernameFormControl: new FormControl('', [Validators.required, Validators.minLength(4), Validators.maxLength(20)]),	
    passwordFormControl: new FormControl('', [Validators.required, Validators.minLength(2), Validators.maxLength(20)]),
  });

  get usernameFormControl() {
    return this.loginForm.controls['usernameFormControl'];
  }

  get passwordFormControl() {
    return this.loginForm.controls['passwordFormControl'];
  }

  onSubmit(){
    const loginDTO: loginDTO = {username: this.usernameFormControl.value, password: this.passwordFormControl.value}
    this.userService.authenticate(loginDTO).subscribe(
      (token: any) => {
      localStorage.setItem('token', token['access']);
      this.router.navigate(['productos/destacada']);}
    )
  }
}
