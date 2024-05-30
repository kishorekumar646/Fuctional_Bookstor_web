from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Products Managing Api''s', ProductView, basename='Book')

urlpatterns = [
    path('', include(router.urls), name='home'),
    # path('product/<slug>/', Products.as_view(), name='product')
]
