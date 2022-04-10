from django import views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework.authentication import BasicAuthentication
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

def home(request):
    posts = Book.objects.all()
    return render(request, 'book/home.html', {'posts':posts})

def about(request):
    return render(request, 'book/about.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Book.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'book/dashboard.html', {'posts':posts, 'full_name':full_name, 'groups':gps})
    else:
        return HttpResponseRedirect('/login')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! You have become an Admin.')
            user = form.save()
            group = Group.objects.get(name='Admin')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'book/signup.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'book/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

def add_book(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                book_name = form.cleaned_data['book_name']
                book_author = form.cleaned_data['book_author']
                book_category = form.cleaned_data['book_category']
                pst= Book(book_name=book_name, book_author=book_author, book_category=book_category)
                pst.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'book/addbook.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

def update_book(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Book.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Book.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'book/updatebook.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

def delete_book(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Book.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


class BookViewset(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


    def get_queryset(self):
        book_specs = Book.objects.all()
        return book_specs