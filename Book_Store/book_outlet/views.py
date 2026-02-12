from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books.order_by("title"),
            # decending add - before field
            "total_books": books.count(),
            "avg_rating": books.aggregate(Avg("rating")),
        },
    )


def book_details(request, slug):
    # try:
    #     book = Book.objects.get(id=_id)
    #     # return render(request, "book_outlet/book_details.html", {"book": book})
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(
        request,
        "book_outlet/book_details.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestselling": book.is_bestselling,
        },
    )
