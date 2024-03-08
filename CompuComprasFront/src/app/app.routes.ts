import { Routes } from '@angular/router';
import { AuthGuard } from './Guards/login-guard.guard';

export const routes: Routes = [
    {
    path: 'productos',
    loadChildren: () => import('./shared/routes').then(m => m.routes),
    canActivate: [
        AuthGuard
    ]
    },
   
    {
        path: '',
        loadChildren: () => import('./modules/user/routes').then(m => m.routes)
    },

    {
        path: '**',
        redirectTo: ''       
    }
];
