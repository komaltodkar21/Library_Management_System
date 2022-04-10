from django.contrib import admin
from .models import Book
from django.contrib.auth.models import User

# Register your models here.
User._meta.get_field('email')._unique = True     #to set unique email
@admin.register(Book)
class BookSpecsAdmin(admin.ModelAdmin):
    list_display = ['id','book_name','book_author','book_category']