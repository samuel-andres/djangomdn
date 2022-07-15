from django.urls import path
from . import views

app_name = 'catalog'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    # path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book/<slug:slug>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('allborrowed/', views.AllBorrowedListView.as_view(), name='all-borrowed'),
]
