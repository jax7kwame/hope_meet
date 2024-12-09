from django.db import models
from tinymce.models import HTMLField

# organization services
class Services(models.Model):
    name = models.CharField(max_length=100)
    description = HTMLField(null=True)
    icon = models.CharField(blank=True, default="bi-person-gear", max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "services"


# team
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='uploads/profile', blank=True)
    position = models.CharField(max_length=100)
    linkedin_link = models.CharField(max_length=255, blank=True)
    ig_link = models.CharField(max_length=255, blank=True)
    fb_link = models.CharField(max_length=255, blank=True)
    x_link = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('position',)

# organization contact
class Contact(models.Model):
    email = models.EmailField()
    telephone = models.CharField(max_length=50, blank=True)
    postal_address = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100)
    ig_link = models.CharField(max_length=255, blank=True)
    fb_link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.email


# About the organization
class About(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='uploads/about/group_logos', blank=True)
    fb_link = models.CharField('facebook link', max_length=255, blank=True)
    ig_link = models.CharField('instagram link', max_length=255, blank=True)
    tiktok_link = models.CharField(max_length=255, blank=True)
    x_link = models.CharField('x link', max_length=255, blank=True)
    banner_image = models.ImageField(upload_to='uploads/about/banner', blank=True)
    description = HTMLField(null=True)
    services_intro = HTMLField(null=True)
    services = models.ManyToManyField(Services, blank=True)
    team = models.ManyToManyField(TeamMember, blank=True)
    contacts = models.ManyToManyField(Contact, blank=True)



    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "about"
    
    #venue_type = models.ForeignKey(VenueType, related_name="venue_types", blank=True, null=True, on_delete=models.SET_NULL)


class Testimonial(models.Model):
    about = models.ForeignKey(About, on_delete=models.SET_NULL, null=True, related_name="testimonials")
    testimonial = models.TextField()
    name = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)


    def __str__(self):
        return self.name
