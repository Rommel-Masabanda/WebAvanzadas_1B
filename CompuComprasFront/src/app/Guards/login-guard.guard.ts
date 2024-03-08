import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private router: Router) {}

  canActivate(): boolean {
    if (localStorage.getItem('token')) {
      console.log(localStorage.getItem('token')); 
      
      return true; // Usuario autenticado, permitir acceso
    } else {
      this.router.navigate(['']); // Redirigir a la página de login si no está autenticado
      return false;
    }
  }
}