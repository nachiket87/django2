from django.shortcuts import render, redirect
from .models import Book
from django.views import generic
from .forms import BookAddForm
from django.contrib import messages


class Home(generic.ListView):
    model = Book
    template_name = 'booklog/home.html'
    context_object_name = 'latest_books'

class Detail(generic.DetailView):
    model = Book
    template_name = 'booklog/detail.html'
    context_object_name = 'latest_books'

def AddBook(request):
    
    form = BookAddForm(request.POST or None)

    if form.is_valid():
        form.save()
        book_title = form.cleaned_data.get('title')
        book_author = form.cleaned_data.get('author')
        messages.success(request, f"{book_title} by {book_author} added!")
        return redirect('books-home')
        
    context = {'form': form}
    return render(request, "booklog/add.html", context)
     