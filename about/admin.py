from django.contrib import admin
from .models import About, Contact, TeamMember, Services, Testimonial

class TestimonialAdmin(admin.TabularInline):
    model = Testimonial


class AboutAdmin(admin.ModelAdmin):
	inlines = [TestimonialAdmin]

# Organizaation admin
admin.site.register(About, AboutAdmin)
admin.site.register(Contact)
admin.site.register(TeamMember)
admin.site.register(Services)

