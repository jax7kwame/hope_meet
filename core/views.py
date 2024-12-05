from django.shortcuts import render
from django.core.paginator import Paginator
from datetime import datetime
import calendar
from calendar import HTMLCalendar

from events.models import Event, EventCategory
from news.models import News


def home_view(request):
    month = datetime.now().month
    ## create "time to the event"

    #query events models for dates
    events_by_month = Event.objects.filter(starting_date__year=datetime.now().year, starting_date__month=month)

    # Featured Events
    featured_events = Event.objects.filter(featured=True, post_event=True).order_by('?')
    featured_paginator = Paginator(featured_events, 1)
    featured_page_number = request.GET.get('page')
    featured_page_obj = featured_paginator.get_page(featured_page_number)

    # event categories
    categories = EventCategory.objects.all()

    # News
    news = News.objects.filter(published=True)

    news_paginator = Paginator(news, 3)
    news_page_number = request.GET.get('page')
    news_page_obj = news_paginator.get_page(news_page_number)


    # month's events per page
    paginator = Paginator(events_by_month, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'featured_events': featured_page_obj,
        'categories': categories,
        'events_by_month': page_obj,
        'news': news_page_obj
    }

    return render(request, 'index.html', context)

 