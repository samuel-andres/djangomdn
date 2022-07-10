from typing import OrderedDict
from django.db import models
from django.urls import reverse
import uuid

class Language(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self) -> str:
        return self.name



class Author(models.Model):
    'attrs'
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died',null=True, blank=True)
    
    '''metadata'''
    class Meta:
        ordering = ['last_name', 'first_name']

    '''methods'''
    def __str__(self) -> str:
        return f'{self.last_name}, {self.first_name}'
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    '''attrs'''
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=1000, help_text='Enter a brief description of the book')
    pubdate = models.DateField('Publication Date')
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                             help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    '''punteros'''
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)    
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    '''metadata'''
    class Meta:
        ordering = ["title", "-pubdate"]

    '''methods'''
    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])



class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    imprint = models.CharField(max_length=200)
    due_back = models.DateField('Expected date of availability',null=True, blank=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Avaible'),
        ('r', 'Reserved'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    '''metadata'''
    class Meta:
        ordering = ['due_back']

    '''punteros'''
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, related_name='get_copies', null=True)

    '''methods'''
    def __str__(self) -> str:
        return f'{self.id} ({self.book.title})'


