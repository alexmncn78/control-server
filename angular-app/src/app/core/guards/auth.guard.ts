import { CanActivateFn } from '@angular/router';
import { inject } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth/auth.service';

export const AuthGuard: CanActivateFn = (route, state) => {
  const authService = inject(AuthService);
  const router = inject(Router);

  if (authService.isAuthtenticated()) {
    return true;
  } else {
    authService.redirectUrl = state.url;
    router.navigate(['/login']);
    return false;
  }
};

