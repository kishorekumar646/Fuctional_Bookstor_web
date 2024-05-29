from django.db import models
from django.utils.safestring import mark_safe
from book_store.validators import *
from django.urls import reverse
from django.db.models.signals import pre_save

CATEGORY = (
    (1, "Programming"),
    (2, "Networking"),
    (3, "Python"),
    (4, "Action and Adventure"),
    (5, "Detective and Mystery"),
    (6, "Historical Fiction"),
    (7, "Fiction"),
)

LABEL_CHOICE = (
    ('P', 'primary'),
    ('S', 'scondary'),
    ('D', 'danger')
)


class Book(models.Model):
    title = models.CharField(
        max_length=255, validators=[BookNameValidator],)
    slug = models.SlugField(unique=True)
    author = models.CharField(
        max_length=255, validators=[BookAuthorValidator],)
    image_cover = models.ImageField(
        upload_to='upload_photos/book_photos/', null=True, blank=True, default=None)
    description = models.CharField(max_length=255, validators=[
        BookNameValidator], null=True, blank=True)
    category = models.PositiveSmallIntegerField(
        choices=CATEGORY, default=None, null=True, blank=True)
    label = models.CharField(max_length=1, default='P',
                             choices=LABEL_CHOICE, null=True, blank=True)
    price = models.FloatField(default=1,null=True,blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.title, self.author)

    def book_photo_thumbnail(self):
        return mark_safe('<img alt="%s" src="%s" width="70" height="120" />' % (self.title, self.image_cover.url))

    def get_absolute_url(self):
        return reverse("product", kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse("add_to_cart", kwargs={'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse("remove_from_cart", kwargs={'slug': self.slug})

    class Meta:
        ordering = ['price']
        verbose_name = 'Book product'
        unique_together = (('title', 'slug'),)
