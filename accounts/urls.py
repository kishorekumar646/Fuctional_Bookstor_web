from django.urls import path, include
from django.urls import path
from .views import Users, AllUsers

urlpatterns = [
    path('user/', AllUsers.as_view(), name='get all user'),
    path('user/<int:pk>/', Users.as_view(), name='get user'),
]
