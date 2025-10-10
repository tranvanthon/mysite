from django.urls import path, include
from accounts.views import profile, edit_profile, edit_avatar


urlpatterns = [
    path('profile/', profile, name='profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('edit/avatar/', edit_avatar, name='edit_avatar'),
    path('', include('allauth.urls')),
]