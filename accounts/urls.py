
from rest_framework.routers import DefaultRouter 
from django.urls import path, include
from django.urls import path
from .views import *

router = DefaultRouter()
router.register('User''s managing api''s', UserView, basename='User Data')
router.register('User''s Documents Managing', UserDocumentView, basename='User Documents')

urlpatterns = [
    path('', include(router.urls), name='get all user'),
    # path('user/<int:pk>/', Users.as_view(), name='get user'),
]
