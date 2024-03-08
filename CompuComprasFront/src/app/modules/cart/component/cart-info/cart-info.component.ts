import { Component, Input } from '@angular/core';
import { CarritoService } from '../../../../services/carrito.service';
import { cartDTO } from '../../../../models/carrito/cartDTO';
import { CartProductDTO } from '../../../../models/carrito/cartProductDTO';
@Component({
  selector: 'app-cart-info',
  standalone: true,
  imports: [],
  templateUrl: './cart-info.component.html',
  styleUrl: './cart-info.component.css'
})
export class CartInfoComponent {
  @Input() item: CartProductDTO = {
    id: 0,
    cantidad: 0,
    carrito: 0,
    producto: 0    
  }
  constructor(private service: CarritoService) { }

  ngOnInit(){
    
  }
  
  getProducto(){
    
  }
}
