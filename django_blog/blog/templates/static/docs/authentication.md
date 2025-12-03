# User Authentication System - Django Blog

## Overview
This document describes the authentication system implemented in the django_blog project.
It covers user registration, login, logout, and profile management.

---

## 1. Registration
- **URL:** `/register/`
- **Form:** `CustomUserCreationForm` (username + email + password)
- **Behavior:**
  - Validates unique username
  - Checks password match
  - Automatically logs in the user after registration

---

## 2. Login
- **URL:** `/login/`
- **Form:** `AuthenticationForm`
- **Behavior:**
  - Validates username/password
  - Provides error messages for invalid login

---

## 3. Logout
- **URL:** `/logout/`
- **Behavior:**
  - Ends user session
  - Redirects to login page
  - Displays confirmation message

---

## 4. Profile Management
- **URL:** `/profile/`
- **Access:** Only logged-in users
- **Behavior:**
  - View current username/email
  - Update email (optional: extend for profile picture/bio)
  - Messages shown for success/failure

---

## 5. Security
- CSRF protection enabled in all forms
- Passwords are securely hashed using Django’s default hashing
- Login required for profile management

---

## 6. How to Test
1. Start server: `python manage.py runserver`
2. Visit `/register/` to create a new account
3. Login via `/login/`
4. Check profile at `/profile/`
5. Logout via `/logout/`

---

## 7. Notes
- Can extend `User` model with a `Profile` model for more fields
- Templates are in `templates/registration/`
