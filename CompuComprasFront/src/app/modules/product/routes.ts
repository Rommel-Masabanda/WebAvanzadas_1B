import { Routes } from "@angular/router";
import { AuthGuard } from "../../Guards/login-guard.guard";
export const routes: Routes = [
    {
        path: '',
        loadComponent: () => import('./pages/list-product/list-product.component').then(m => m.ListProductComponent)
    }
]