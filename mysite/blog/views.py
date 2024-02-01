from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post


def post_list(request):
    # получаем QuerySet со списком наших постов
    post_list = Post.published.all()

    # раздробляем этот список по 5 обьекта(поста) на страницу
    paginator = Paginator(post_list, 5)

    # получаем данные из GET запроса с парамтром page, или используем 1 как дефолтное значение
    page_number = request.GET.get("page", 1)

    try:
        # передаем в posts список постов с конкретной страницой через page_number
        posts = paginator.page(page_number)

    except PageNotAnInteger:
        # если в GET запросе не цифра на строка то вернуть 1 страницу
        posts = paginator.page(1)
        
    except EmptyPage:
        # Если page_number находится вне диапазона, то
        # выдать последнюю страницу
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=post,
    )
    return render(request, "blog/post/detail.html", {"post": post})
