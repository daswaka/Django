from django.db import models
from organizer.models import Startup, Tag
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=60, unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField(help_text='date published', auto_now_add=True) # auto adds the date
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, related_name='blog_posts')

    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date','title']
        get_latest_by = 'pub_date'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'year': self.pub_date.year, 
                                            'month':self.pub_date.month, 'slug':self.slug})

    def __str__(self):
        return f'{self.title} : {self.pub_date.strftime('%Y-%m-%d')}'
