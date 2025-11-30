from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# --------------------------------------------
# List all books (read-only for everyone)
# --------------------------------------------
class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Retrieves a list of all books.
    Accessible to anyone (unauthenticated users allowed).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# --------------------------------------------
# Retrieve single book by ID
# --------------------------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<int:pk>/
    Retrieve details of a single book by its ID.
    Accessible to anyone (unauthenticated users allowed).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# --------------------------------------------
# Create a new book (authenticated users only)
# --------------------------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Create a new book.
    Only authenticated users can create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom hook to run additional logic on creation.
        """
        serializer.save()


# --------------------------------------------
# Update an existing book (authenticated users only)
# --------------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /api/books/<int:pk>/update/
    Update an existing book.
    Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom hook to run additional logic on update.
        """
        serializer.save()


# --------------------------------------------
# Delete a book (authenticated users only)
# --------------------------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<int:pk>/delete/
    Delete a book instance.
    Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        """
        Custom hook to run additional logic before deletion.
        """
        instance.delete()
