from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from app.models import Post


def index(request: HttpRequest) -> HttpResponse:
    qs = [{"id": 1, "title": "post #1"}]
    return render(request, "app/index.html", {"post_list": qs})


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    return render(
        request,
        "app/post_detail.html",
        {
            "post": post,
        },
    )
