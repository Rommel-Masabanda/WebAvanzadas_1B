import { Component, Input } from '@angular/core';
import { NavbarComponent } from '../../../../shared/navbar/navbar.component';
import { ProductoGet } from '../../../../models/producto/productoGet';
import { CarritoService } from '../../../../services/carrito.service';
import { ProductoAddDTO } from '../../../../models/producto/productoAddDTO';
@Component({
  selector: 'app-info-product',
  standalone: true,
  imports: [NavbarComponent],
  templateUrl: './info-product.component.html',
  styleUrl: './info-product.component.css'
})
export class InfoProductComponent {
  @Input() producto: ProductoGet = {
    id: 0,
    titulo: "",
    descripcion: "",
    precio: 0,
    categoria: "",
    imagen: ""
  };

  constructor(private carritoService: CarritoService) { }

  agregarAlCarrito(id: number) {
    const product: ProductoAddDTO = {
      producto_id: id,
      cantidad: 1
    }
    this.carritoService.saveCarrito(product).subscribe()
  }

}
