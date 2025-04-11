from django.views.generic import ListView, CreateView, View
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Author, Book, BorrowRecord
from .forms import AuthorForms, BookForms, BorrowRecordForms
from .utils import export_to_excel

class AuthorListView(ListView):
    model = Author
    template_name = 'libraryapp/author_list.html'
    paginate_by = 10
    ordering = ['id'] 

class BookListView(ListView):
    model = Book
    template_name = 'libraryapp/book_list.html'
    paginate_by = 10
    ordering=['published_date']

class BorrowRecordListView(ListView):
    model = BorrowRecord
    template_name = 'libraryapp/borrowrecord_list.html'
    paginate_by = 10
    ordering=['return_date']

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForms
    template_name = 'libraryapp/add_author.html'
    success_url = reverse_lazy('author-list')

    def form_invalid(self, form):
        print("Form Errors:", form.errors)  # Debug here
        return super().form_invalid(form)


class BookCreateView(CreateView):
    model = Book
    form_class = BookForms
    template_name = 'libraryapp/add_book.html'
    success_url = reverse_lazy('book-list')

class BorrowRecordCreateView(CreateView):
    model = BorrowRecord
    form_class = BorrowRecordForms
    template_name = 'libraryapp/add_borrowrecord.html'
    success_url = reverse_lazy('borrowrecord-list')

class ExportExcelView(View):
    def get(self, request):
        return export_to_excel()
