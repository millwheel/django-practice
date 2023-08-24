from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    qs = [{"id": 1, "title": "post #1"}]
    return render(request, "app/index.html", {"post_list": qs})
