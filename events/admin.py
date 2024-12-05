from django.contrib import admin
from .models import Event, EventCategory, Venue, ChurchOrGroup, VenueType, County, Speaker, SponsorPartner


class SpeakerAdmin(admin.TabularInline):
    model = Speaker

class SponsorPartnerAdmin(admin.TabularInline):
    model = SponsorPartner

class EventCategoryAdmin(admin.ModelAdmin):
    ordering = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {
        'slug': ('title',)
    }


class EventAdmin(admin.ModelAdmin):
    inlines = [SpeakerAdmin, SponsorPartnerAdmin]
    list_display = ['title', 'category', 'post_event', 'featured', 'starting_date', 'ending_date', 'county_local']
    list_filter = ('category', 'created_at', 'church_or_group', 'manager')
    search_fields = ('title', 'district', 'description', 'manager')
    ordering = ('-created_at',)
    prepopulated_fields = {
        'slug': ('title',)
    }


class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'phone']
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