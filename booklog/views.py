from django.shortcuts import render, HttpResponse
from .models import Book
from django.views import generic
from .forms import BookAddForm


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
        
    context = {'form': form}
    return render(request, "booklog/add.html", context)
     