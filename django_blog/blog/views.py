from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

# --------------------------
# Home Page
# --------------------------
def home(request):
    """
    Render the home page.
    Shows a welcome message and login/register links if user is anonymous.
    """
    context = {
        "user": request.user if request.user.is_authenticated else None
    }
    return render(request, "blog/home.html", context)

# --------------------------
# User Registration
# --------------------------
def register_view(request):
    """
    Handle user registration.
    Extends Django's UserCreationForm to include email.
    Logs in the user automatically after successful registration.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})

# --------------------------
# User Login
# --------------------------
def login_view(request):
    """
    Handle user login using Django's built-in AuthenticationForm.
    Provides error feedback for invalid credentials.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("profile")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})

# --------------------------
# User Logout
# --------------------------
def logout_view(request):
    """
    Logs out the user and redirects to the login page.
    """
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect("login")

# --------------------------
# User Profile Management
# --------------------------
@login_required
def profile_view(request):
    """
    Allow authenticated users to view and update their profile.
    Currently allows updating the email.
    """
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            request.user.email = email
            request.user.save()
            messages.success(request, "Profile updated successfully.")
    return render(request, "registration/profile.html", {"user": request.user})



