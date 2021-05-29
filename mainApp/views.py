from django.shortcuts import render, redirect
from .models import *


def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'index.html', context)


def addBook(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )
    return redirect('/')


def addAuthor(request, id):
    Author.objects.create(
        book = Book.objects.get(id = request.POST['book_id']),
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes']
    )
    return render(request, 'authors.html')


def viewBook(request, id):
    context = {
        "book": Book.objects.get(id = id),
        # "authors": Author.objects.get(id = id)
    }
    print (Book.objects.get(id = id))
    return render(request, 'books.html', context)


def viewAuthor(request, id):
    context = {
        "author": Author.objects.get(id = id)
    }
    print (Author.objects.get(id = id))
    return render(request, 'authors.html', context)


def delete_book(request, id):
    book = Book.objects.get(id = id)
    book.delete()

    return redirect('/')


def delete_author(request):
    author = Author.objects.get(id = id)
    author.delete()

    return redirect('authors/')