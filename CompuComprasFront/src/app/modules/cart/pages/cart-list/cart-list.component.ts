import { Component } from '@angular/core';
import { CartInfoComponent } from '../../component/cart-info/cart-info.component';
import { ActivatedRoute } from '@angular/router';
import { CarritoService } from '../../../../services/carrito.service';
import { cartDTO } from '../../../../models/carrito/cartDTO';
import { CartProductDTO } from '../../../../models/carrito/cartProductDTO';
@Component({
  selector: 'app-cart-list',
  standalone: true,
  imports: [CartInfoComponent],
  templateUrl: './cart-list.component.html',
  styleUrl: './cart-list.component.css'
})
export class CartListComponent {

  constructor(private router: ActivatedRoute, private cartService:CarritoService) { }
  protected carritoList: CartProductDTO[] = [];
  ngOnInit(){
    this.getCarrito();
  }

  id: number = 0
  getCarrito(){
    this.cartService.getCarrito().subscribe((carrito) => {
      const cartDTO: cartDTO = carrito;
      this.id = cartDTO.carritos[0].id
      this.carritoList = cartDTO.carrito_productos
      console.log("log de carrito list")
      console.log(this.carritoList);});
  }
  
}
