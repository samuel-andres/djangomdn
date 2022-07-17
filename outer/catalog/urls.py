from django.urls import path
from . import views

app_name = 'catalog'
urlpatterns = [
    # HOMEPAGE
    path('', views.IndexView.as_view(), name='index'),
    # LIST VIEWS
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('allborrowed/', views.AllBorrowedListView.as_view(), name='all-borrowed'),
    # DETAIL VIEWS
    path('book/<slug:slug>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('profile/<slug:slug>', views.ProfileView.as_view(), name='user-profile'),
    # CUD VIEWS
    path('create/author/', views.AuthorCreate.as_view(), name='author-create'),
    path('update/author/<int:pk>',
         views.AuthorUpdate.as_view(), name='author-update'),
    path('delete/author/<int:pk>',
         views.AuthorDelete.as_view(), name='author-delete'),
    path('create/book/', views.BookCreate.as_view(), name='book-create'),
    path('update/book/<slug:slug>', views.BookUpdate.as_view(), name='book-update'),
    path('delete/book/<slug:slug>', views.BookDelete.as_view(), name='book-delete'),
    #     path('update/profile/<slug:slug>',
    path('update/profile/',
         views.UpdateProfileView.as_view(), name='update-profile'),
    path('create/profile/', views.CreateProfileView.as_view(), name='create-profile'),
    #     path("create/profile/", views.CreateProfileView.as_view(), name="create-profile"),
    # forms.py VIEWS
    path('book/<uuid:pk>/renew/', views.BookRenewView.as_view(), name='book-renew'),
    path('social/members', views.ProfileListView.as_view(), name='profile-list'),
    path('book/<uuid:pk>/borrow/',
         views.BorrowBookInstanceView.as_view(), name='book-borrow'),
    path('alltoborrow/', views.AllToBorrowListView.as_view(), name='all-toborrow'),
]
