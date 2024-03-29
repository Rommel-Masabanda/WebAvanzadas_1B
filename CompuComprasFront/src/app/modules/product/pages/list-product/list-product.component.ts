import { Component } from '@angular/core';
import { NavbarComponent } from '../../../../shared/navbar/navbar.component';
import { InfoProductComponent } from '../../component/info-product/info-product.component';
import { ActivatedRoute } from '@angular/router';
import { ProductoGet } from '../../../../models/producto/productoGet';
import { ProductService } from '../../../../services/product.service';
import { CarritoService } from '../../../../services/carrito.service';
import { cartDTO } from '../../../../models/carrito/cartDTO';
@Component({
  selector: 'app-list-product',
  standalone: true,
  imports: [NavbarComponent, InfoProductComponent],
  templateUrl: './list-product.component.html',
  styleUrl: './list-product.component.css'
})
export class ListProductComponent {
  
  constructor(private router: ActivatedRoute, private productService:ProductService, private cartService:CarritoService) { }
  category = "";

    productos: ProductoGet[] = []
    private type = this.router.params.subscribe(params => {
      console.log(params['category']);
      this.category = params['category'];
      this.productService.getProducts().subscribe(
        (productos) => this.productos = productos
      )
    })  

    ngOnInit(){
      this.getCarrito();
    }
  
    getCarrito(){
      this.cartService.getCarrito().subscribe((carrito) => {
        const cartDTO: cartDTO = carrito;
        console.log(cartDTO.carritos[0].id);});
    }
  
  
}
