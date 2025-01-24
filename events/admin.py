from django.contrib import admin
from .models import Event, EventCategory, Venue, ChurchOrGroup, VenueType, County, Speaker, SponsorPartner, VenueImages, Union, Conference, PhotoGallery, GuestChoir



class PhotoGalleryAdmin(admin.TabularInline):
    model = PhotoGallery

class SpeakerAdmin(admin.TabularInline):
    model = Speaker

class GuestChoirAdmin(admin.TabularInline):
    model = GuestChoir

class SponsorPartnerAdmin(admin.TabularInline):
    model = SponsorPartner

class EventCategoryAdmin(admin.ModelAdmin):
    ordering = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {
        'slug': ('title',)
    }


class EventAdmin(admin.ModelAdmin):
    inlines = [SpeakerAdmin, GuestChoirAdmin, SponsorPartnerAdmin, PhotoGalleryAdmin]
    list_display = ['title', 'category', 'post_event', 'featured', 'starting_date', 'ending_date', 'county_local']
    list_filter = ('category', 'created_at', 'church_or_group', 'manager')
    search_fields = ('title', 'district', 'description', 'manager')
    ordering = ('-created_at',)
    prepopulated_fields = {
        'slug': ('title',)
    }


class VenueImagesAdmin(admin.TabularInline):
    model = VenueImages

class VenueAdmin(admin.ModelAdmin):
    inlines = [VenueImagesAdmin,]
    list_display = ['name', 'venue_type', 'phone']
    search_fields = ('name', 'location', 'type', 'address')
    prepopulated_fields = {
        'slug': ('name',)
    }


class ChurchOrGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }

class CountyAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }




# Regitering models
admin.site.register(Event, EventAdmin)
admin.site.register(EventCategory, EventCategoryAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(ChurchOrGroup, ChurchOrGroupAdmin)
admin.site.register(VenueType)
admin.site.register(County, CountyAdmin)
admin.site.register(Union)
admin.site.register(Conference)