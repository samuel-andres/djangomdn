import re
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.views import View, generic
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from .models import Book, Author, BookInstance, Genre

class IndexView(View):
    def get(self, request):
        """View function for home page of site."""

        # Generate counts of some of the main objects
        num_books = Book.objects.all().count()
        num_instances = BookInstance.objects.all().count()

        # Available books (status = 'a')
        num_instances_available = BookInstance.objects.filter(status__exact='a').count()

        # The 'all()' is implied by default.
        num_authors = Author.objects.count()

        nobooks_cont_the = Book.objects.filter(title__icontains='the').count()
        nogen_that_sw_caph = Genre.objects.filter(name__startswith='H').count()

        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1


        context = {
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'nobooks_cont_the':nobooks_cont_the,
            'nogen_that_sw_caph':nogen_that_sw_caph,
            'num_visits': num_visits + 1,

        }

        return render(request, 'catalog/index.htm', context=context)

class BookListView(generic.ListView):
    model = Book
    template_name = 'catalog/book_list.htm'
    context_object_name = 'book_list'
    paginate_by = 10

    queryset = Book.objects.all().order_by('author__name')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['today'] = datetime.now()
        return context

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/author_list.htm'

# @login_required se usa para func based views
class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author
    template_name = 'catalog/author_detail.htm'
    #loginmixin
    login_url = 'login'


# class BookDetailView(View):
#     def get(self, request, slug):
#         try:
#             actual_book = Book.objects.get(slug__exact=slug)
#             context = {
#                 'title' : actual_book.title,
#                 'summary': actual_book.summary,
#             }
#             return render(request, 'catalog/book_detail.htm', context)
#         except: raise Http404('Book does not exist')


class BookDetailView(View):
    def get(self, request, slug):
        actual_book = get_object_or_404(Book, slug=slug)
        avaible_copies = actual_book.bookinstance_set.all().filter(status='a')
        ordered_rest = actual_book.bookinstance_set.all().exclude(status='a').order_by('due_back')

        context = {
            'book' : actual_book,
            'avaible_copies': avaible_copies,
            'ordered_rest': ordered_rest,
        }
        return render(request, 'catalog/book_detail.htm', context)

