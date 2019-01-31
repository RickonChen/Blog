from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Tag(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(default='', blank=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('tag', args=[str(self.slug)])
