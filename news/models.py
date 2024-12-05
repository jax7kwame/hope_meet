from django.db import models
from tinymce.models import HTMLField


# News model 
class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    author = models.CharField(max_length=100, blank=True)
    #news_author = models.ForeigmKey()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/news')
    intro = HTMLField()
    body = HTMLField()
    youtube_video = models.CharField(max_length=255, blank=True)
    random_quote = models.TextField()
    quote_author = models.CharField(max_length=255)

    published = models.BooleanField()
    featured = models.BooleanField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created_at',)

