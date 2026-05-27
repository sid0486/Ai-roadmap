import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../core/services/auth.service';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './register.component.html'
})
export class RegisterComponent {
  username = '';
  email = '';
  password = '';
  error = '';
  success = '';
  loading = false;

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit(): void {
    this.error = '';
    this.success = '';
    this.loading = true;

    this.authService.register({
      username: this.username,
      email: this.email,
      password: this.password
    }).subscribe({
      next: () => {
        this.success = 'Account created! Redirecting to login...';
        setTimeout(() => this.router.navigate(['/login']), 1500);
      },
      error: (err) => {
        const status = err.status;
        if (status === 400) {
          this.error = 'An account with this email already exists. Please login instead.';
        } else {
          this.error = err.error?.detail || 'Registration failed. Please try again.';
        }
        this.loading = false;
      }
    });
  }
}