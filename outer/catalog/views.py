'''python built in libs'''
from dataclasses import fields
from datetime import *
from multiprocessing import context
from django.forms import ModelForm

''' net stuff'''
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy

''' auth stuff'''
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

''' Views, forms and models'''
from catalog.forms import RenewBookForm
from django.views import View, generic
from .models import Book, Author, BookInstance, Genre
from django.contrib.auth.models import User

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

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.htm'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class AllBorrowedListView(PermissionRequiredMixin, generic.ListView):
    permission_required = (
        'catalog.can_mark_returned',
    )

    model = BookInstance
    template_name = 'catalog/all_borrowed_list_view.htm'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


class BookRenewView(PermissionRequiredMixin,View):
    permission_required = (
        'catalog.can_mark_returned',
    )

    form_class = RenewBookForm
    template_name = 'catalog/book_renew.htm'
    initial = {}


    def get(self, request, pk):
        proposed_renewal_date = date.today() + timedelta(weeks=3)
        self.initial['renewal_date'] = proposed_renewal_date
        form = self.form_class(initial=self.initial)

        context = {
            'form':form,
            'book_instance': get_object_or_404(BookInstance, pk=pk),
        }


        return render(request, self.template_name, context)

    def post(self, request, pk):
        # retrieve the book_instance
        book_instance = get_object_or_404(BookInstance, pk=pk)
        # retrieve the form with the data entered by the user
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data> and store it 
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            return HttpResponseRedirect(reverse('catalog:all-borrowed'))

        context = {
            'form' : form,
            'book_instance' : book_instance,   
        }


        return render(request, self.template_name, context)


class AuthorCreate(PermissionRequiredMixin,generic.edit.CreateView):
    permission_required = (
        'catalog.can_crud_authors',
    )
    model = Author

    fields = [
        'first_name',
        'last_name',
        'date_of_birth',
        'date_of_death',
        'authpic',
    ]

    initial = {
        'date_of_death': '11/06/2020'
    }

class AuthorUpdate(generic.edit.UpdateView):
    model = Author
    # using the __all__ is a bad practice
    fields = '__all__'

class AuthorDelete(generic.edit.DeleteView):
    model = Author
    success_url = reverse_lazy('catalog:author-list')
    