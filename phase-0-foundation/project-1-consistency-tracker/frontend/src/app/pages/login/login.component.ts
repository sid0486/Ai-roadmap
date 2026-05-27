import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../core/services/auth.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './login.component.html'
})
export class LoginComponent {
  email = '';
  password = '';
  error = '';
  loading = false;

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit(): void {
    this.error = '';
    this.loading = true;

    this.authService.login({ username: this.email, password: this.password })
      .subscribe({
        next: () => this.router.navigate(['/dashboard']),
        error: (err) => {
          const status = err.status;
          if (status === 401) {
            this.error = 'Incorrect password. Please try again.';
          } else if (status === 404) {
            this.error = 'No account found with this email.';
          } else {
            this.error = err.error?.detail || 'Login failed. Please try again.';
          }
          this.loading = false;
        }
      });
  }
}