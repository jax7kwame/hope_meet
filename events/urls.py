from django.urls import path
from .views import event_detail_view, events_view, category_view, venues_view, venue_detail_view, search_venues_view, church_or_group_view, search_events_view, venue_events_view, month_events_view, county_view, like_event, dislike_event, tag_event_list

urlpatterns = [
    path("search_venues/", search_venues_view, name="search_venues"),
    path("search_events/", search_events_view, name="search_events"),
    path("events/", events_view, name="events"),
    path("event/<slug:category_slug>/<slug:slug>/", event_detail_view, name="event_details"),
    path('events/tag/<slug:tag_slug>/', tag_event_list, name='tag_events'),
    path('like-event/<slug:category_slug>/<slug:slug>/', like_event, name="like_event"),
    path('dislike-event/<slug:category_slug>/<slug:slug>/', dislike_event, name="dislike_event"),
    path("events/this_month/", month_events_view, name="month_events"),
    #path("all_categories/", all_categories_view, name="all_categories"),
    path('category/<slug:slug>/', category_view, name="category"),
    path('county/<slug:slug>/', county_view, name="county"),
    path('church-or-group/<slug:slug>/', church_or_group_view, name='group_events'),
    #path("add_venue/", add_venue, name="add_venue"),
    path("all-venues/", venues_view, name='venues'),
    path("venue_details/<slug:slug>/", venue_detail_view, name='venue_detail'),
    path("venue_events/<slug:slug>/", venue_events_view, name='venue_events')
]
