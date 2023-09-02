from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import  *

def index(request):
    if request.method == 'POST' :
        add_book =  BookForm(request.POST)
        if add_book.is_valid() :
            add_book.save()
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    

    context={
        'book' : Book.objects.all(),
        'category' : Category.objects.all(),
        'form' :BookForm(),
        'catform': CategoryForm(),
        'all_books':Book.objects.filter(available=True).count,
        'sold_books' : Book.objects.filter(status='sold').count,
        'rent_books' : Book.objects.filter(status='rental').count,
        'available_books' : Book.objects.filter(status='available').count,
    }
    return render(request , 'pages/index.html',context)


def books(request):
    search = Book.objects.all()
    title = None 
    if 'search_name' in request.GET :
        title = request.GET['search_name']
        if title :
            search = search.filter(title__icontains=title)

    context = {
        'book':search,
        'category' : Category.objects.all(),
    }
    return render(request,'pages/books.html',context)


def delete(request,id):
    book_delete = get_object_or_404(Book , id=id) # this function perofrme like the other one , it takes the model and an attriute name and gets that attribute from that model
    if request.method == 'POST' :
        book_delete.delete()
        return redirect('/')
    
    return render(request,'pages/delete.html')


def update(request,id):
    book_id = Book.objects.get(id=id) #this variable only get the id of specific book that we want to update 
    if request.method == 'POST':        
        book_save = BookForm(request.POST,instance=book_id) # here we send the data of that book to the database to save it 
        if book_save.is_valid() :
            book_save.save() # we confirm the process if the data entered is valid
            return redirect('/')

    else:
        book_save = BookForm(instance=book_id) 

    context = {
        'bookform' : book_save,
    }
    return render(request,'pages/update.html',context)




# Create your views here.
