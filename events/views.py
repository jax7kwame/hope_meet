from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator
from django.urls import reverse
from taggit.models import Tag

from datetime import datetime
from .models import Event, EventCategory, Venue, ChurchOrGroup, County
#from .forms import VenueForm


# search venue view
def search_venues_view(request):
    query = request.GET.get('query', '')

    venues = Venue.objects.filter(Q(name__icontains=query) | Q(type__icontains=query) | Q(location__icontains=query) | Q(description__icontains=query))

    # venues per page
    paginator = Paginator(venues, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query
    }

    return render(request, 'search_venues.html', context)


#search_events
def search_events_view(request):
    query = request.GET.get('query', '')

    events = Event.objects.filter(Q(title__icontains=query) | Q(church_or_group__name__icontains=query) | Q(district__icontains=query) | Q(venue__name__icontains=query) | Q(description__icontains=query))

    paginator = Paginator(events, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query
    }

    return render(request, 'search_events.html', context)


# events list view
def events_view(request):
    events = Event.objects.filter(post_event=True)
    categories = EventCategory.objects.all()
    # events per page
    paginator = Paginator(events, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        #"events": events,
        'categories': categories,
        'page_obj': page_obj
    }
    return render(request, 'events.html', context)


# event detail view
def event_detail_view(request, category_slug, slug):
    event = get_object_or_404(Event, slug=slug)
    similar_events = Event.objects.filter(category=event.category)
    speakers = event.event_speakers.all()
    sponsors_partners = event.event_sponsors_partners.all()
    photo_gallery = event.event_gallery.all()
    #group = get_object_or_404(ChurchOrGroup, slug=slug)

    context = {
        "event": event,
        'similar_events': similar_events,
        'speakers': speakers,
        'sponsors_partners': sponsors_partners,
        'photo_gallery': photo_gallery
        #"group": group
    }

    return render(request, 'event.html', context)


# tags and products
def tag_event_list(request, tag_slug=None):
    events = Event.objects.filter(post_event=True).order_by('-id')

    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        events = events.filter(tags__in=[tag])
    
    context = {
        'events': events,
        'tag': tag
    }

    return render(request, 'tag-events.html', context)



# category view
def category_view(request, slug):
    category = get_object_or_404(EventCategory, slug=slug)
    print(category)

    context = {
        "category": category
    }

    return render(request, 'category.html', context)


# county view
def county_view(request, slug):
    county = get_object_or_404(County, slug=slug)

    context = {
        'county': county
    }

    return render(request, 'county_events.html', context)


# church_or group view
def church_or_group_view(request, slug):
    group = get_object_or_404(ChurchOrGroup, slug=slug)

    context = {
        "group": group
    }

    return render(request, 'church_or_group.html', context)


# All venues view
def venues_view(request):
    venues = Venue.objects.all().order_by('name')
    # events per page
    paginator = Paginator(venues, 11)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }

    return render(request, 'venues.html', context)


# Venue details view
def venue_detail_view(request, slug):
    venue = get_object_or_404(Venue, slug=slug)
    venue_images = venue.venue_images.all()

    context = {
        'venue': venue,
        'venue_images': venue_images,
    }

    return render(request, 'venue.html', context)

# Venue events
def venue_events_view(request, slug):
    venue = get_object_or_404(Venue, slug=slug)

    context = {
        'venue': venue,
    }

    return render(request, 'venue_events.html', context)


# current month events view
def month_events_view(request):

    month = datetime.now().month
    month_name=datetime.now().strftime('%B')
    
    #query events models for dates
    events_by_month = Event.objects.filter(starting_date__year=datetime.now().year, starting_date__month=month)

    # events per page
    paginator = Paginator(events_by_month, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "month_name": month_name.capitalize()
    }
    return render(request, 'month_events.html', context)

# add venue view
'''
def add_venue(request):
    submitted = False

    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:  
        form = VenueForm
        
        if submitted in request.GET:
            submitted = True

    context = {
        "form": form,
        'submitted': submitted
    }
    return render(request, 'add_venue.html', context)
'''

@csrf_exempt
@login_required(login_url="login")
def like_event(request, category_slug, slug):
    user = request.user
    like = False

    if request.method == "POST":
        event_id = request.POST['eventId']
        event = get_object_or_404(Event, slug=slug)

        if user not in event.dislikes.all():
            if user in event.likes.all():
                event.likes.remove(user)
                like = False
            else:
                event.likes.add(user)
                like = True
            
            data = {
                'liked': like,
                'likes_count': event.likes.all().count()
            }

            return JsonResponse(data, safe=False)
        else:
            pass
    
    return redirect(reverse('event_details', args=[category_slug, slug]))


@csrf_exempt
@login_required(login_url="login")
def dislike_event(request, category_slug, slug):
    user = request.user
    dislike = False

    if request.method == "POST":
        event_id = request.POST['eventId']
        event = get_object_or_404(Event, slug=slug)

        if user not in event.likes.all():
            if user in event.dislikes.all():
                event.dislikes.remove(user)
                dislike = False
            else:
                event.dislikes.add(user)
                dislike = True
            
            data = {
                'disliked': dislike,
                'dislikes_count': event.dislikes.all().count()
            }

            return JsonResponse(data, safe=False)
        else:
            pass
    
    return redirect(reverse('event_details', args=[category_slug, slug]))