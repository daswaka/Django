from django.db import models
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=31, help_text="A label for URL config")

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.title()


class Startup(models.Model):
    name = models.CharField(max_length=50, db_index=True) # ensure name does not exceed 50 characters
    slug = models.CharField(unique=True)
    description = models.TextField()
    founded_date = models.DateField(help_text='Date founded') # ensures data entered looks like a valid date
    email = models.EmailField(help_text='Email') # ensures data entered looks like a valid email address
    website = models.URLField(max_length=255) # ensures data entered looks like a valid URL
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL,null=True, blank=True) # a one-to-many relationship

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'

    def get_absolute_url(self):
        return reverse('startup_detail', kwargs={'slug':self.slug})

    def __str__(self):
        return self.name


class NewsLink(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField(help_text='Date published', auto_now_add=True)
    link = models.URLField(max_length=255)
    startup = models.ManyToManyField(Startup) # a many-to-many relationship

    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'

    def __str__(self):
        return f'{self.startup} : {self.title}'



