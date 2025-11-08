from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm 
from .models import Book, Library
from .forms import RegisterForm


# ------------------------
# Book and Library Views
# ------------------------

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# ------------------------
# Authentication Views
# ------------------------

# Login using Django's built-in LoginView
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'


# Logout using Django's built-in LogoutView
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


# Custom registration view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('list_books')  # Redirect to book list after signup
    else:
        form = RegisterForm()
    return render(request, 'relationship_app/register.html', {'form': form})
