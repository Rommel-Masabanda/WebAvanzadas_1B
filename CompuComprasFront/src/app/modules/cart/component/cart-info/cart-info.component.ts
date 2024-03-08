import { Component, Input } from '@angular/core';
import { CarritoService } from '../../../../services/carrito.service';
import { cartDTO } from '../../../../models/carrito/cartDTO';
import { CartProductDTO } from '../../../../models/carrito/cartProductDTO';
import { ProductService } from '../../../../services/product.service';
import { ProductoGet } from '../../../../models/producto/productoGet';
import { deleteDTO } from '../../../../models/carrito/deleteProductoDTO';
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

  protected producto: ProductoGet = {
    id: 0,
    titulo: "",
    descripcion: "",
    precio: 0,
    categoria: "",
    imagen: ""
  }

  constructor(private service: ProductService, private carritoService: CarritoService) { }

  ngOnInit(){
   this.getProducto() 
  }
  
  getProducto(){
    this.service.getProduct(this.item.producto).subscribe(
      (producto) => this.producto = producto
    )
  }

  eliminarDelCarrito(){
    const deleteP: deleteDTO = {
      item_carrito_id: this.item.id
    }
    this.carritoService.deleteCarrito(deleteP).subscribe(() => window.location.reload())
  }
}
