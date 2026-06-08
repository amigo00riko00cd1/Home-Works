from django.shortcuts import redirect, render

books_dir = {
    1: "Book 1",
    2: "Book 2",
    3: "Book 3",
}

writers_dir = {
    "1": "Writer",
    "2": "Writer",
    "3": "Writer"
}


# Create your views here.
def main_page(request):
    return render(request, 'main/main.html')

def writers(request):
    return render(request, 'writers/writers.html', {"writers" : writers_dir})

def top_best_books(request):
    return render(request, 'topBestBooks/topBestBooks.html', {"books": books_dir})

def writer_info(request, surname):

    writers = list(writers_dir.items())
    writer = next((x for x in writers if x[0] == surname), None)

    if writer == None:
        return redirect("writers")

    return render(request, 'writers/writerInfo.html', {'writer': writer})

def book_info(request, topBestBooks):

    book = books_dir.get(topBestBooks)

    if book == None:
        return redirect("top_best_books")


    return render(request, 'topBestBooks/book.html', {"book":book})