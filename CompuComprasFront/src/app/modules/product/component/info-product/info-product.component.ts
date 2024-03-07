import { Component, Input } from '@angular/core';
import { NavbarComponent } from '../../../../shared/navbar/navbar.component';
import { ProductoGet } from '../../../../models/producto/productoGet';

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
}
