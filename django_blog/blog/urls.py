from django.urls import path
from .views import LoginView, register, LogoutView, profile, edit_profile

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile' ),
]