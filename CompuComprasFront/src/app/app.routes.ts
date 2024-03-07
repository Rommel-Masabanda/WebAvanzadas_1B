import { Routes } from '@angular/router';

export const routes: Routes = [
    {
    path: 'productos',
    loadChildren: () => import('./shared/routes').then(m => m.routes)
    },
   
    {
        path: '**',
        redirectTo: 'productos/destacada'
    }
];
