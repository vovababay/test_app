from django.contrib import admin
from testapp.models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_birth')

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'published')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)