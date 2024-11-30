import csv

from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import BookSerializer
from apps.books.models import Book


class BookViewSet(viewsets.ViewSet):
    @swagger_auto_schema(request_body=BookSerializer)
    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        books = Book.objects.all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="books.csv"'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Title', 'Author', 'Published Date', 'Price'])
        for book in books:
            writer.writerow([book.id, book.title, book.author, book.published_date, book.price])
        return response

    @swagger_auto_schema(request_body=BookSerializer)
    def update(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
