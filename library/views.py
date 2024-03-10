from django.shortcuts import render
from django.views import View
from .models import Book


# Create your views here.
class BookListView(View):
    def get(self, request):
        search = request.GET.get("search_book_name")
        if search is None:
            books = Book.objects.all()
            context = {"books": books}
            return render(request, "library/book_list.html", context)

        else:
            books = Book.objects.filter(title__icontains=search) | Book.objects.filter(description__icontains=search)
            context = {"books": books, "search": search}
            return render(request, "library/book_list.html", context)


class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        context = {"book": book,
                   "id":id}
        return render(request, "library/book_detail.html", context)
