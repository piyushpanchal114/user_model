from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_form, name='login'),
    path('signup/', views.signup_form, name='signup'),
    path('users/', views.users_detail, name='users'),
]
