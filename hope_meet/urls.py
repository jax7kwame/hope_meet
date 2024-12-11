
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('hopemeet-admin/secure-login/', admin.site.urls),
    path('', include('about.urls')),
    path('', include("core.urls")),
    path('', include('events.urls')),
    path('', include('news.urls')),
    
    path('', include('contact.urls')),
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Hopemeet administration"
admin.site.index_title = "Welcome to hopemeet admin site"
