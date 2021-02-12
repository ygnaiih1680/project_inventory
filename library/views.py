from django.shortcuts import render


def library(request):
    return render(request, "library.html")


def library_add(request, isbn):
    title = request.POST["title"]
    contents = request.POST["contents"]
    authors = request.POST["authors"]
    url = request.POST["url"]

    param = {
        "isbn": isbn,
        "title": title,
        "contents": contents,
        "authors": authors,
        "url": url,
    }

    return render(request, "library_add.html", param)
