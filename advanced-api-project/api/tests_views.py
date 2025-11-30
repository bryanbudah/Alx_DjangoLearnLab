from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

        # Create test author
        self.author = Author.objects.create(name="John Doe")

        # Create test books
        self.book1 = Book.objects.create(title="Django Basics", publication_year=2023, author=self.author)
        self.book2 = Book.objects.create(title="Advanced DRF", publication_year=2024, author=self.author)

    # ---------------------------
    # Test: List Books
    # ---------------------------
    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # ---------------------------
    # Test: Retrieve Single Book
    # ---------------------------
    def test_retrieve_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # ---------------------------
    # Test: Create Book (Authenticated)
    # ---------------------------
    def test_create_book_authenticated(self):
        url = reverse("book-create")
        data = {"title": "New Book", "publication_year": 2025, "author": self.author.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "New Book")

    # ---------------------------
    # Test: Update Book (Authenticated)
    # ---------------------------
    def test_update_book_authenticated(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Updated Book", "publication_year": 2023, "author": self.author.id}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    # ---------------------------
    # Test: Delete Book (Authenticated)
    # ---------------------------
    def test_delete_book_authenticated(self):
        url = reverse("book-delete", args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------------------------
    # Test: Permissions (Unauthenticated)
    # ---------------------------
    def test_create_book_unauthenticated(self):
        self.client.logout()
        url = reverse("book-create")
        data = {"title": "Unauthorized Book", "publication_year": 2025, "author": self.author.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------------------
    # Test: Filtering
    # ---------------------------
    def test_filter_books_by_title(self):
        url = reverse("book-list") + "?title=Advanced DRF"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Advanced DRF")

    # ---------------------------
    # Test: Search
    # ---------------------------
    def test_search_books_by_title(self):
        url = reverse("book-list") + "?search=Django"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Django Basics")

    # ---------------------------
    # Test: Ordering
    # ---------------------------
    def test_order_books_by_publication_year_desc(self):
        url = reverse("book-list") + "?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Advanced DRF")

