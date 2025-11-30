from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

# --------------------------------------------
# List all books (read-only for unauthenticated users)
# --------------------------------------------
class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    List all books. Read-only for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# --------------------------------------------
# Retrieve a single book by ID
# --------------------------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<int:pk>/
    Retrieve a single book. Read-only for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# --------------------------------------------
# Create a new book (authenticated only)
# --------------------------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Create a new book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom hook for additional logic on creation.
        """
        serializer.save()


# --------------------------------------------
# Update an existing book (authenticated only)
# --------------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /api/books/<int:pk>/update/
    Update a book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom hook for additional logic on update.
        """
        serializer.save()


# --------------------------------------------
# Delete a book (authenticated only)
# --------------------------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/<int:pk>/delete/
    Delete a book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        """
        Custom hook for additional logic before deletion.
        """
        instance.delete()

