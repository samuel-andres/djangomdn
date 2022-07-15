from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

class BooksInLine(admin.StackedInline):
    model = Book
    extra = 0

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    '''The fields attribute lists just those fields that are to be displayed on the form, in order. Fields are displayed vertically by default, but will display horizontally if you further group them in a tuple (as shown in the "date" fields above).'''
    '''list_display is for the general view, fields for the detail'''
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death'), 'authpic']
    inlines = [BooksInLine]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

'''muestra las instancias en el form/detail de Book, vertically'''
class BooksInstanceInLine(admin.TabularInline):
    model = BookInstance
    '''extra sirve para que no muestre campos vacíos'''
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    '''author use the dunder methot str defined in the model
    display_genre is used bc is a many2many field'''
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInLine]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'borrower' ,'due_back', 'id')
    ''' fieldsets son diferentes secciones dentro del form/detalle'''
    fieldsets = (
        ('Book Data', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )



admin.site.register(Genre)