import { Component } from '@angular/core';
import { CartInfoComponent } from '../../component/cart-info/cart-info.component';
import { ActivatedRoute } from '@angular/router';
import { CarritoService } from '../../../../services/carrito.service';
import { cartDTO } from '../../../../models/carrito/cartDTO';
@Component({
  selector: 'app-cart-list',
  standalone: true,
  imports: [CartInfoComponent],
  templateUrl: './cart-list.component.html',
  styleUrl: './cart-list.component.css'
})
export class CartListComponent {

  constructor(private router: ActivatedRoute, private cartService:CarritoService) { }
  
  ngOnInit(){
    this.getCarrito();
  }

  getCarrito(){
    this.cartService.getCarrito().subscribe((carrito) => {
      const cartDTO: cartDTO = carrito;
      console.log(cartDTO.carritos[0]);});
  }
  
}
