from django.urls import path
from .views import *

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/add/', AuthorCreateView.as_view(), name='author-add'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/add/', BookCreateView.as_view(), name='book-add'),
    path('borrowrecords/', BorrowRecordListView.as_view(), name='borrowrecord-list'),
    path('borrowrecords/add/', BorrowRecordCreateView.as_view(), name='borrowrecord-add'),
    path('export/excel/', ExportExcelView.as_view(), name='export-excel'),
]
