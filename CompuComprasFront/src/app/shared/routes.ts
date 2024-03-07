import { Routes } from "@angular/router";

export const routes: Routes = [
    {
        path: '',
        loadComponent: () => import('./navbar/navbar.component').then(m => m.NavbarComponent),
        children: [
            {
                path: ':category',
                loadComponent: () => import('../modules/product/pages/list-product/list-product.component').then(m => m.ListProductComponent)
            }
        ]
    }
]