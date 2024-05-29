from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


USER_TYPE_CHOICES = (
    (1, 'Administrator'),
    (2, 'Distributor Executive'),
    (3, 'Distributor Manager'),
    (4, 'Operation Executive'),
    (5, 'Operation Manager'),
    (6, 'Sales Executive'),
    (7, 'Sales Manager'),
)

USER_DOCUMENTS_TYPE_CHOICES = (
    ("pc", "PAN Card"),
    ("dl", "Driving License"),
    ("uidai", "Aadhaar Card"),
    ("pp", "Passport"),
    ("vc", "Voter Card"),
)


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, phone_number, password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone_number:
            raise ValueError('The given phone must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        """Create and save a regular User with the given phone and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, password, **extra_fields)


class User(AbstractUser):
    """User model."""
    username = None
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    phone_regex = RegexValidator(
        regex=r'^[6-9]\d{9}$', message="Phone number is not valid")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=10, blank=False, unique=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)
    user_photo = models.ImageField(
        upload_to='upload_photos/user_photos/', null=True, blank=True)
    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES, default='6', null=True)
    last_login_date = models.DateField(auto_now_add=True)
    imei_no = models.CharField(max_length=20, null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    objects = UserManager()

    class Meta:
        ordering = ['-id']
        verbose_name = "User"
        # unique_together = ("first_name", "last_name", )

    def profile_photo(self):
        return mark_safe('<img src="{}" alt="{}" width="90" height="80" />'.format(self.user_photo.url, self.phone_number))

    def __str__(self):
        return "%s - %s" % (str(self.phone_number), self.first_name)


class UserWithName(User):
    class Meta:
        proxy = True

    def __str__(self):
        if self.first_name and self.last_name:
            return "%s - %s %s" % (
                str(self.phone_number), self.first_name, self.last_name
            )

        elif self.first_name:
            return "%s - %s" % (str(self.phone_number), self.first_name)

        return "%s" % (str(self.phone_number))


class UserDocument(models.Model):
    user = models.ForeignKey(
        User, related_name='user_documents', on_delete=models.CASCADE)
    user_document_type = models.CharField(
        max_length=100, choices=USER_DOCUMENTS_TYPE_CHOICES, default='uidai')
    user_document_number = models.CharField(max_length=100)
    user_document_photo = models.FileField(
        upload_to='upload_photos/documents/')

    def user_document_photo_thumbnail(self):
        return mark_safe('<img alt="%s" src="%s" width="70" height="120" />' % (self.user, self.user_document_photo.url))

    def __str__(self):
        return "%s - %s" % (self.user, self.user_document_number)

    class Meta:
        ordering = ['-id']
        verbose_name = "User Document"
