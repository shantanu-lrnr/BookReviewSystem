from django.shortcuts import render,redirect
from .forms import BookForm
from .models import Book
from django.contrib import messages

# Create your views here.

def book_create(request):
    if request.method=='POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Book created successfully')
            return redirect('book-create')
    else:
        form = BookForm()
    return render(request,'book/book_form.html',{'form':form})

def book_list(request):
    genre = request.GET.get('genre')
    if genre:
        books = Book.objects.filter(genre=genre).order_by('-created_at')
    else:
        books = Book.objects.all().order_by('-created_at')
    return render(request,'book/book_list.html',{'books':books})

def book_detail(request,id):
    book = Book.objects.get(pk=id)
    return render(request,'book/book_detail.html',{'book':book})

def book_update(request,id):
    if request.method == 'POST':
        book = Book.objects.get(pk=id)
        form = BookForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            messages.success(request,'Book updated successfully!')
            return redirect('book-update', id=book.id)
    else:
        book = Book.objects.get(pk=id)
        form = BookForm(instance=book)
    return render(request,'book/book_update.html',{'form':form})

def book_delete(request,id):
    if request.method == 'POST':
        book = Book.objects.get(pk=id)
        book.delete()
        messages.success(request,'Book Deleted successfully!')
        return redirect('book-list')
    else:
        return render(request,'book/delete_sure.html',{'id':id})
    

    

