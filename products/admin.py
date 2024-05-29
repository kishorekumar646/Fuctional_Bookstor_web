from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ''''   
    Book details in admin page   
    '''
    fieldsets = (
        (_('Book info'), {'fields': (('title', 'author'), 'description', 'category', 'label',
                                     ('image_cover', 'book_photo_thumbnail'), 'price', 'slug')}),
        (_('Important dates'), {'fields': ('created_at', 'modified_at')}),
    )
    list_display = ('id', 'title', 'author', 'price', 'label', 'created_at', 'modified_at')
    list_filter = ('price', 'created_at', 'modified_at')
    search_fields = ('book_title', 'book_author')
    radio_fields = {'category': admin.HORIZONTAL}
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'modified_at', 'book_photo_thumbnail',)
    list_per_page = 10
