from django.db import models
from account.models import Account
from phone_field import PhoneField
from datetime import date, datetime
from tinymce.models import HTMLField


# county
class County(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        ordering=("name",) 
        verbose_name_plural = "Counties"



# events category model
class EventCategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    icon_style = models.TextField(blank=True, default="bi bi-calendar2-event")

    def __str__(self):
        return self.title
    

    class Meta:
        ordering=("title",) 
        verbose_name_plural = "Categories"


# Venue type model
class VenueType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

# Venue modes
class Venue(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to='uploads/venue', blank=True, null= True)

    venue_type = models.ForeignKey(VenueType, related_name="venue_types", blank=True, null=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=100)
    county = models.ForeignKey(County, blank=True, null=True, related_name="venues", on_delete=models.SET_NULL)
    address = models.CharField(max_length=100, blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(blank=True)
    website_url = models.URLField(blank=True)
    fb_link = models.CharField('facebook link', max_length=255, blank=True)
    ig_link = models.CharField('instagram link', max_length=255, blank=True)
    x_link = models.CharField('x link', max_length=255, blank=True)
    description = HTMLField(null=True, blank=True)

    def __str__(self):
        return self.name

class VenueImages(models.Model):
    image = models.ImageField(upload_to="uploads/venue", blank=True, null=True)
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, related_name="venue_images")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Venue Images'

# conference
class Conference(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

# union
class Union(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class ChurchOrGroup(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    logo = models.ImageField(upload_to='uploads/group_logos', blank=True)
    district = models.CharField(max_length=100, blank=True)
    conference = models.ForeignKey(Conference, null=True, on_delete=models.SET_NULL, blank=True)
    union = models.ForeignKey(Union, null=True, on_delete=models.SET_NULL, blank=True)
    website_url = models.URLField(blank=True)
    fb_link = models.CharField('facebook link', max_length=255, blank=True)
    ig_link = models.CharField('instagram link', max_length=255, blank=True)
    x_link = models.CharField('x link', max_length=255, blank=True)
    youtube_link = models.CharField('youtube link', max_length=255, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)


# events model table
class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to='uploads/events', blank=True)
    category = models.ForeignKey(EventCategory, related_name="events", null=True, on_delete=models.SET_NULL)
    
    
    starting_date = models.DateField()
    ending_date = models.DateField(blank=True, null=True)
    starting_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
    church_or_group = models.ForeignKey(ChurchOrGroup, related_name='events', null=True, on_delete=models.SET_NULL)

    description = HTMLField(null=True)
    venue = models.ForeignKey(Venue, blank=True, related_name="events", null=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=100)
    #county = models.CharField(max_length=100)
    county_local = models.ForeignKey(County, blank=True, null=True, related_name="events", on_delete=models.SET_NULL)



    created_at = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey(Account, blank=True, null=True, on_delete=models.SET_NULL, related_name="events")
    featured = models.BooleanField(default=False)
    post_event = models.BooleanField(default=False)
    likes = models.ManyToManyField(Account, blank=True, related_name="video_liked")
    dislikes = models.ManyToManyField(Account, blank=True, related_name="video_disliked")

    class Meta:
        ordering = ('-created_at',)


    def __str__(self):
        return self.title
    
    @property
    def num_likes(self):
        return self.likes.count()
    
    @property
    def num_dislikes(self):
        return self.dislikes.count()

    
    @property
    def remaining_days(self):
        d1 = datetime.strptime(str(self.starting_date), "%Y-%m-%d")
        d2 = datetime.now()
        days_till = d1 - d2

        if int(days_till.days) > 0:
            return f"({days_till.days} days remaining)"
        elif int(days_till.days) == 0:
            return "(today)"
        else:
            return "(Passed)"
    @property
    def days_till(self):
        d1 = datetime.strptime(str(self.starting_date), "%Y-%m-%d")
        d2 = datetime.now()
        days_to = int((d1 - d2).days)

        return days_to

    @property
    def event_duration(self):
        if self.ending_date:
            d1 = datetime.strptime(str(self.starting_date), "%Y-%m-%d")
            d2 = datetime.strptime(str(self.ending_date), "%Y-%m-%d")

            duration = int((d2 - d1).days) + 1

            if duration > 1:
                return f"{duration} days event"
            elif duration == 1:
                return f"{duration} day event"
            else:
                return "duration not defined"
        else:
            return "1 day event"

# event photo gallery
class PhotoGallery(models.Model):
    event =  models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_gallery")
    image = models.ImageField(upload_to="uploads/gallery", blank=True, null=True)

    def __str__(self):
        return self.event.title
    
    class Meta:
        verbose_name_plural = 'Photo gallery'


# speaker
class Speaker(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, related_name="event_speakers")
    image = models.ImageField(upload_to='uploads/speakers', blank=True, null= True)
    title = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=50)
    topic = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

# sponsors and patners
class SponsorPartner(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, related_name="event_sponsors_partners")
    logo = models.ImageField(upload_to='uploads/sponsors_partners', blank=True, null= True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name