import { Component } from '@angular/core';
import { RouterOutlet, RouterLink, Router} from '@angular/router';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [RouterOutlet, RouterLink],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {

    constructor(private router: Router) { }
    
    logout(){
        localStorage.clear();
        this.router.navigate(['']);
    }
}
