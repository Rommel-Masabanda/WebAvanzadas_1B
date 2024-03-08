import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../environments/environment.development';
import { Observable } from 'rxjs';
import { ProductoGet } from '../models/producto/productoGet';
import { getTokenLS } from '../utils/user';
@Injectable({
  providedIn: 'root'
})
export class ProductService {

  private readonly = `${environment.apiUrl}producto/`;
  constructor(private http: HttpClient) { }

  getProducts():Observable<ProductoGet[]> {
    return this.http.get<ProductoGet[]>(this.readonly, {headers: {'Authorization': `Bearer ${getTokenLS()}`}});
  }
}
