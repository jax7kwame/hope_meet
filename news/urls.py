from django.urls import path
from .views import all_news_view, news_article_view

urlpatterns = [
    path('all_news_articles/', all_news_view, name="all_news"),
    path('news/<slug:slug>/', news_article_view, name="news_article")
]
