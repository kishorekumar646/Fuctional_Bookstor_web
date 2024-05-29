from django.contrib import admin
from .models import User, UserDocument, UserWithName
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (_('Personal info'), {'fields': (('user_photo', 'profile_photo',), ('first_name', 'last_name',),
                                         'phone_number', 'email',
                                         'password')}),
        (_('Permissions'), {'fields': ('user_type', 'is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('phone_number', 'email', 'first_name',
                    'last_name', 'date_joined', 'imei_no', 'is_superuser')
    list_filter = ('is_superuser', 'is_staff', 'is_active')
    search_fields = ('phone_number', 'email', 'first_name', 'last_name')
    readonly_fields = ('profile_photo', 'imei_no',)
    ordering = ('date_joined',)
    list_per_page = 10


@admin.register(UserDocument)
class UserDocumentAdmin(admin.ModelAdmin):
    fieldsets =(
        (_('User documents Info'),{'fields': ('user','user_document_type', 'user_document_number',
              ('user_document_photo', 'user_document_photo_thumbnail',),)}),
    )
    readonly_fields = ('user_document_photo_thumbnail',)


@admin.register(UserWithName)
class UserWithNameAdmin(admin.ModelAdmin):
    model = UserWithName
    fieldsets = (
        (_('Personal info'), {'fields': (('user_photo', 'profile_photo',), ('first_name', 'last_name',), 'phone_number', 'email')}),
    )
    search_fields = ('phone_number', 'email', 'first_name', 'last_name')
    list_display = ('phone_number', 'email', 'first_name', 'last_name', 'date_joined', 'imei_no', 'is_superuser')
    readonly_fields = ('profile_photo', 'imei_no',)


admin.site.unregister(Group)
