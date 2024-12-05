from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published', 'featured']
    list_filter = ('created_at', 'published', 'featured', 'author')
    search_fields = ('title', 'author')
    ordering = ('-created_at',)
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(News, NewsAdmin)

