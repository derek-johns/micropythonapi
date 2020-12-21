from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'author', 'user', 'rating', 'reviews', 'price', 'year', 'genre')
