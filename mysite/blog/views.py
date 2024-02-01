from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    """
    Альтернативное представление списка постов
    """

    # атрибут queryset используется для того, чтобы иметь конкретно-при-
    # кладной набор запросов QuerySet, не извлекая все объекты. Вместо
    # определения атрибута queryset мы могли бы указать model=Post, и Django
    # сформировал бы для нас типовой набор запросов Post.objects.all();
    queryset = Post.published.all()

    # контекстная переменная posts используется для результатов запроса.
    # Если не указано имя контекстного объекта context_object_name, то по
    # умолчанию используется переменная object_list;
    context_object_name = "posts"

    # в атрибуте paginate_by задается постраничная разбивка результатов
    # с возвратом трех объектов на страницу;
    paginate_by = 3

    # конкретно-прикладной шаблон используется для прорисовки страницы
    # шаблоном template_name. Если шаблон не задан, то по умолчанию List-
    # View будет использовать blog/post_list.html
    template_name = "blog/post/list.html"


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
