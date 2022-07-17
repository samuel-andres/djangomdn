########################### IMPORTS ################################
# python built in libs
from datetime import *
from re import template
from sre_constants import SUCCESS
from webbrowser import get
# net stuff
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
# auth stuff
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
# Views, forms and models
from django.views import View, generic

from .models import Book, Author, BookInstance, Genre, Language, UserProfile
from catalog.forms import RenewBookForm, CreateBookForm, CreateProfileForm
from django import forms

from django.contrib.auth.models import Group, User


from catalog.user import UserCreateView, UserUpdateView
########################### HOMEPAGE ################################


class IndexView(View):
    def get(self, request):
        """View function for home page of site."""

        # Generate counts of some of the main objects
        num_books = Book.objects.all().count()
        num_instances = BookInstance.objects.all().count()

        # Available books (status = 'a')
        num_instances_available = BookInstance.objects.filter(
            status__exact='a').count()

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
            'nobooks_cont_the': nobooks_cont_the,
            'nogen_that_sw_caph': nogen_that_sw_caph,
            'num_visits': num_visits + 1,

        }

        return render(request, 'catalog/index.htm', context=context)

########################### LIST VIEWS ################################
############BOOK###########


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


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.htm'
    paginate_by = 10

    # el get_queryset es el método de la vista genérica que obtiene los objetos de la base de datos,
    # acá lo sobreescribí llamando al método en la clase padre (super) y modificando su retorno para
    # que solo me devuelva los que son del usuario actual, on loan y ordenados por fecha de devolución

    def get_queryset(self):
        qs = super(LoanedBooksByUserListView, self).get_queryset()
        # return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
        return qs.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class AllBorrowedListView(PermissionRequiredMixin, generic.ListView):
    permission_required = (
        # 'catalog.can_mark_returned',
        'catalog.is_librarian',
    )

    model = BookInstance
    template_name = 'catalog/all_borrowed_list_view.htm'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


class AllToBorrowListView(AllBorrowedListView):
    template_name = 'catalog/all_toborrow_list_view.htm'

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='a').order_by('book__title')

############AUTOR###########


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/author_list.htm'

########################### DETAIL VIEWS ################################
############BOOK###########


# class BookDetailView(View):

class BookDetailView(PermissionRequiredMixin, View):
    permission_required = (
        'catalog.is_library_member',
        # 'can_view_detailed_books',
    )

    def get(self, request, slug):
        actual_book = get_object_or_404(Book, slug=slug)
        avaible_copies = actual_book.bookinstance_set.all().filter(status='a')
        ordered_rest = actual_book.bookinstance_set.all().exclude(
            status='a').order_by('due_back')

        context = {
            'book': actual_book,
            'avaible_copies': avaible_copies,
            'ordered_rest': ordered_rest,
        }
        return render(request, 'catalog/book_detail.htm', context)

############AUTHOR###########


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    # @login_required se usa para func based views
    model = Author
    template_name = 'catalog/author_detail.htm'
    # loginmixin
    login_url = 'login'
###########USERPROFILE########


class ProfileView(generic.DetailView):
    ''' detail view del profile'''
    model = UserProfile
    template_name = 'catalog/profile.htm'


class ProfileListView(generic.ListView):
    model = UserProfile
    template_name = 'catalog/profile_list.htm'

# class UpdateProfileView(generic.edit.UpdateView):
#     model = UserProfile
#     form_class = CreateProfileForm
#     template_name = 'catalog/userprofile_form.html'


# el problema con esta vista es que no está restringiendo el acceso a editar
# solo nuestra información, es decir, si desde un usuario hardcodeo el link para editar
# otro usuario rompo todo
# class UpdateProfileView(LoginRequiredMixin, View):
#     model = UserProfile
#     template = 'catalog/userprofile_form.html'

#     def get(self, request, slug):
#         actual_profile = get_object_or_404(self.model, slug=slug)
#         form = CreateProfileForm(instance=actual_profile)
#         ctx = {
#             'form': form,
#         }
#         return render(request, self.template, ctx)

#     def post(self, request, slug):
#         actual_profile = get_object_or_404(self.model, slug=slug)
#         form = CreateProfileForm(
#             request.POST, request.FILES, instance=actual_profile)
#         print('REQUEEEEEEEEEEEEEEEST', request)
#         if not form.is_valid:
#             ctx = {
#                 'form': form,
#             }
#             return render(request, self.template, ctx)

#         form.save()
#         library_member = Group.objects.get(name='Library Member')
#         library_member.user_set.add(actual_profile.user)
#         return redirect('catalog:user-profile', slug)

class UpdateProfileView(UserUpdateView):
    model = UserProfile
    form_class = CreateProfileForm


class CreateProfileView(UserCreateView):
    model = UserProfile
    form_class = CreateProfileForm


########################### CUD VIEWS ################################
############AUTHOR###########


class AuthorCreate(PermissionRequiredMixin, generic.edit.CreateView):
    permission_required = (
        # 'catalog.can_crud_authors',
        'catalog.is_librarian',
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


class AuthorUpdate(PermissionRequiredMixin, generic.edit.UpdateView):
    permission_required = (
        # 'catalog.can_crud_authors',
        'catalog.is_librarian',
    )
    model = Author
    # using the __all__ is a bad practice
    fields = '__all__'


class AuthorDelete(PermissionRequiredMixin, generic.edit.DeleteView):
    permission_required = (
        # 'catalog.can_crud_authors',
        'catalog.is_librarian',
    )
    model = Author
    success_url = reverse_lazy('catalog:author-list')

############BOOK###########


class BookCreate(PermissionRequiredMixin, generic.edit.CreateView):
    permission_required = (
        # 'catalog.can_crud_books',
        'catalog.is_librarian',
    )

    model = Book

    initial = {
        'isbn': '0000000000000',
    }

    form_class = CreateBookForm
    template_name = 'catalog/book_form.htm'
    # success_url = reverse_lazy('catalog:author-detail')


class BookUpdate(PermissionRequiredMixin, generic.edit.UpdateView):
    permission_required = (
        # 'catalog.can_crud_books',
        'catalog.is_librarian',
    )

    model = Book
    form_class = CreateBookForm
    template_name = 'catalog/book_form.htm'


class BookDelete(PermissionRequiredMixin, generic.edit.DeleteView):
    permission_required = (
        # 'catalog.can_crud_books',
        'catalog.is_librarian',
    )

    model = Book
    success_url = reverse_lazy('catalog:book-detail')
    template_name = 'catalog/book_confirm_delete.htm'


########################### forms.py VIEWS ################################
############BOOK###########


# class BorrowBookInstanceView(PermissionRequiredMixin, View):
#     permission_required = (
#         'catalog.is_librarian',
#     )

#     form_class = BorrowBookForm
#     template_name = 'catalog/borrow_book.htm'
#     initial = {}

#     def get(self, request, pk):
#         proposed_renewal_date = date.today() + timedelta(weeks=3)
#         self.initial['renewal_date'] = proposed_renewal_date
#         form = self.form_class(initial=self.initial)

#         context = {
#             'form': form,
#         }

#         return render(request, self.template_name, context)

#     def post(self, request):
#         # retrieve the book_instance
#         book_instance = get_object_or_404(
#             BookInstance, pk=request.POST['book_instance_field'])
#         # retrieve the form with the data entered by the user
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             # <process form cleaned data> and store it
#             book_instance.borrower = User.objects.get(
#                 username=form.cleaned_data['borrower_field'])
#             book_instance.due_back = form.cleaned_data['renewal_date']
#             book_instance.save()

#             return HttpResponseRedirect(reverse('catalog:all-borrowed'))

#         context = {
#             'form': form,
#             'book_instance': book_instance,
#         }

#         return render(request, self.template_name, context)


class BookRenewView(PermissionRequiredMixin, View):
    permission_required = (
        # 'catalog.can_mark_returned',
        'catalog.is_librarian',
    )

    form_class = RenewBookForm
    template_name = 'catalog/book_renew.htm'
    initial = {}

    def get(self, request, pk):
        proposed_renewal_date = date.today() + timedelta(weeks=3)
        self.initial['renewal_date'] = proposed_renewal_date
        actual_borrower = User.objects.get(
            username=get_object_or_404(BookInstance, pk=pk).borrower)
        self.initial['borrower_field'] = actual_borrower
        form = self.form_class(initial=self.initial)

        context = {
            'form': form,
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
            book_instance.borrower = User.objects.get(
                username=form.cleaned_data['borrower_field'])
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            return HttpResponseRedirect(reverse('catalog:all-borrowed'))

        context = {
            'form': form,
            'book_instance': book_instance,
        }

        return render(request, self.template_name, context)


class BorrowBookInstanceView(BookRenewView):
    template_name = 'catalog/book_borrow.htm'

    def get(self, request, pk):
        proposed_renewal_date = date.today() + timedelta(weeks=3)
        self.initial['renewal_date'] = proposed_renewal_date
        form = self.form_class(initial=self.initial)

        context = {
            'form': form,
            'book_instance': get_object_or_404(BookInstance, pk=pk),
        }

        return render(request, self.template_name, context)
