from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Serializes individual book data.
# Includes custom validation to ensure publication year is not in the future.
class BookSerializer(serializers.ModelSerializer):

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = '__all__'


# Serializes the Author model and nests BookSerializer to show related books.
# Uses related_name 'books' defined in Book model.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
