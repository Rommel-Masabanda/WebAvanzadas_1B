import { Routes } from "@angular/router";

export const routes: Routes = [
    {
        path: '',
        loadComponent: () => import('./pages/list-product/list-product.component').then(m => m.ListProductComponent)
    }
]