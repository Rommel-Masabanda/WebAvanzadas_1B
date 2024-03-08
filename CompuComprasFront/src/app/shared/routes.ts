import { Routes } from "@angular/router";

export const routes: Routes = [
    {
        path: '',
        loadComponent: () => import('./navbar/navbar.component').then(m => m.NavbarComponent),
        children: [
            {
                path: 'carrito',
                loadComponent: () => import('../modules/cart/pages/cart-list/cart-list.component').then(m => m.CartListComponent)
            },
            
            {
                path: ':category',
                loadComponent: () => import('../modules/product/pages/list-product/list-product.component').then(m => m.ListProductComponent)
            }
            
        ]
    }
]