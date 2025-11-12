from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

# Create a new book - requires can_create permission
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # validates and sanitizes input
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})


# Edit an existing book - requires can_edit permission
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)  # safely fetch the book
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():  # validates and sanitizes input
        form.save()
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html', {'form': form})


# Optional: View book list - requires can_view permission
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # safe ORM query
    return render(request, 'bookshelf/book_list.html',  {'books': books})
