import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment.development';
import { Observable } from 'rxjs';
import { loginDTO } from '../models/login/loginDTO';
@Injectable({
  providedIn: 'root'
})
export class UserService {
  private readonly authUrl = `${environment.tokenApi}`
  constructor(private http: HttpClient) { }

  authenticate(loginDTO: loginDTO): Observable<any> {
    return this.http.post<any>(this.authUrl, loginDTO);
  }


}
