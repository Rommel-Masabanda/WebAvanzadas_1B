import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { UserService } from '../../../services/user.service';
import { loginDTO } from '../../../models/login/loginDTO';
import { Router, RouterLink } from '@angular/router';
import { RegisterDTO } from '../../../models/login/registerDTO';
    
@Component({
  selector: 'app-register-component',
  standalone: true,
  imports: [ReactiveFormsModule, RouterLink],
  templateUrl: './register-component.component.html',
  styleUrl: './register-component.component.css'
})
export class RegisterComponentComponent {

  
  constructor(private registerService:UserService, private router: Router) { }
  readonly registerForm: FormGroup = new FormGroup({
    usernameFormControl: new FormControl('', [Validators.required, Validators.minLength(4), Validators.maxLength(20)]),
    correoFormControl: new FormControl('', [Validators.required, Validators.email]),	
    passwordFormControl: new FormControl('', [Validators.required, Validators.minLength(2), Validators.maxLength(20)]),
  });

  get usernameFormControl() {
    return this.registerForm.controls['usernameFormControl'];
  }
  get correoFormControl() {
    return this.registerForm.controls['correoFormControl'];
  }

  get passwordFormControl() {
    return this.registerForm.controls['passwordFormControl'];
  }

  onSubmit(){
    const register: RegisterDTO = {username: this.usernameFormControl.value,  password: this.passwordFormControl.value, email: this.correoFormControl.value}
    this.registerService.register(register).subscribe(()=>
      this.router.navigate([''])
    )
  }
}
