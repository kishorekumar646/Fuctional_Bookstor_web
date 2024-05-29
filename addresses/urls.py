from django.urls import path
from .views import Addresses

urlpatterns = [
    path('', Addresses.as_view(), name='All Adresses'),
    path('product/<slug>/', Addresses.as_view(), name='get address by id'),
]
