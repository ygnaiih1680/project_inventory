from django.shortcuts import render
from django.conf import settings
import json
import requests as req


def book(request):
    return render(request, "book_info.html")


def search(request):
    search_text = request.GET["book-search"]
    criteria = request.GET["search-criteria"]
    url = "https://dapi.kakao.com/v3/search/book"
    headers = {
        "Authorization": f"KakaoAK {settings.KAKAO_REST_API_KEY}"
    }
    if search_text == "":
        return render(request, 'index.html', {"error": "input text"})
    params = {
        "sort": "accuracy",
        "query": search_text,
        "page": 1,
        "size": 12,
    }
    if criteria != "":
        params["target"] = criteria
    books = json.loads(req.get(url=url, params=params, headers=headers).text)["documents"]
    return render(request, 'book_info.html', {"books": books})