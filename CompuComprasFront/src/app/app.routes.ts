import { Routes } from '@angular/router';

export const routes: Routes = [
    {
    path: 'list',
    loadChildren: () => import('./shared/routes').then(m => m.routes)
    },
    {
    path: 'product',
    loadChildren: () => import('./modules/product/routes').then(m => m.routes)
    },
    {
        path: '**',
        redirectTo: 'list'
    }
];
