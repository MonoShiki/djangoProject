from django.urls import path
from .views import register, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/',  auth_views.LoginView.as_view(template_name='c_auth/login.html'), name='sign_in'),
    path('log_out/', auth_views.LogoutView.as_view(template_name='c_auth/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
]
