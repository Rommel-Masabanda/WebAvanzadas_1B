import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment.development';
import { Observable } from 'rxjs';
import { loginDTO } from '../models/login/loginDTO';
import { RegisterDTO } from '../models/login/registerDTO';
@Injectable({
  providedIn: 'root'
})
export class UserService {
  private readonly authUrl = `${environment.tokenApi}`
  private readonly registerUrl = `${environment.registerUrl}`
  constructor(private http: HttpClient) { }

  authenticate(loginDTO: loginDTO): Observable<any> {
    return this.http.post<any>(this.authUrl, loginDTO);
  }

  register(register: RegisterDTO): Observable<any> {
    return this.http.post<any>(this.registerUrl, register);
  }

}
