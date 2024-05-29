from django.urls import path
from .views import Products

urlpatterns = [
    path('', Products.as_view(), name='home'),
    path('product/<slug>/', Products.as_view(), name='product')
]
