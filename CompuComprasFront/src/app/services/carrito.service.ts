import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment.development';
import { Observable } from 'rxjs';
import { cartDTO } from '../models/carrito/cartDTO';
import { getTokenLS } from '../utils/user';
import { ProductoAddDTO } from '../models/producto/productoAddDTO';
import { deleteDTO } from '../models/carrito/deleteProductoDTO';
import { realizarCompraDTO } from '../models/carrito/realizarCompraDTO';
@Injectable({
  providedIn: 'root'
})
export class CarritoService {
  private readonly urlCarrito = `${environment.apiUrl}obtenerCarrito/`
  private readonly addCarrito = `${environment.apiUrl}agregar-producto-al-carrito/`
  private readonly deleteCarrit = `${environment.apiUrl}eliminarProductosCarrito/`
  private readonly realizarCom = `${environment.apiUrl}realizarCompra/`
  constructor(private http: HttpClient) { }

  getCarrito(): Observable<cartDTO> {
    return this.http.get<cartDTO>(this.urlCarrito, {headers: {'Authorization': `Bearer ${getTokenLS()}`}});
  }

  saveCarrito(ProductoAddDTO: ProductoAddDTO): Observable<any> {
    return this.http.post<any>(this.addCarrito, ProductoAddDTO, {headers: {'Authorization': `Bearer ${getTokenLS()}`}});
  }

  deleteCarrito(deleteCarrito: deleteDTO): Observable<any> {
    return this.http.post<any>(this.deleteCarrit, deleteCarrito, {headers: {'Authorization': `Bearer ${getTokenLS()}`}});
  }

  realizarCompra(realizar: realizarCompraDTO): Observable<any> {
    return this.http.post<any>(this.realizarCom, realizar, {headers: {'Authorization': `Bearer ${getTokenLS()}`}});
  }
}
