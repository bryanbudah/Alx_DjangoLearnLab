from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import views for register, list_books, LibraryDetailView

urlpatterns = [
    # Book and Library URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs (must use built-in LoginView/LogoutView directly)
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]


