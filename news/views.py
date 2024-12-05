from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News


# All News
def all_news_view(request):
    news = News.objects.filter(published=True)
    # news articles per page
    news_paginator = Paginator(news, 7)
    news_page_number = request.GET.get('page')
    news_page_obj = news_paginator.get_page(news_page_number)

    context = {
        'news_page_obj': news_page_obj
    }

    return render(request, 'all_news.html', context)


def news_article_view(request, slug):
    news_article = get_object_or_404(News, slug=slug)
    news = News.objects.filter(published=True, featured=False)
    # news articles per page
    news_paginator = Paginator(news, 4)
    news_page_number = request.GET.get('page')
    news_page_obj = news_paginator.get_page(news_page_number)

    context = {
        'news_article': news_article,
        'news_page_obj': news_page_obj
    }

    return render(request, 'news_article.html', context)