import { Component } from '@angular/core';
import { NavbarComponent } from '../../../../shared/navbar/navbar.component';
import { InfoProductComponent } from '../../component/info-product/info-product.component';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-list-product',
  standalone: true,
  imports: [NavbarComponent, InfoProductComponent],
  templateUrl: './list-product.component.html',
  styleUrl: './list-product.component.css'
})
export class ListProductComponent {
  
  constructor(private router: ActivatedRoute) { }
  mensaje = "a";
  
    private type = this.router.params.subscribe(params => {
      console.log(params['id']);
      this.mensaje = params['id'];
    })  
  
  
  
  
  
}
