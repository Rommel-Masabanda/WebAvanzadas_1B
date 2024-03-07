import { Routes } from '@angular/router';

export const routes: Routes = [
    {
    path: '',
    loadComponent: () => import('./login-component/login-component.component').then(m => m.LoginComponentComponent)
    },
    {
        path: 'register',
        loadComponent: () => import('./register-component/register-component.component').then(m => m.RegisterComponentComponent)
    } 
];
