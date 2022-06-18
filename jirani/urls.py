from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('', views.index, name='index'),
  path('register/', views.register, name='register'),
  path("logout/", LogoutView.as_view(), name="logout"),
  path('profile/<username>/', views.profile, name='profile'),
  path('profile/<username>/edit', views.edit_profile, name='edit'),
  path('create-hood/', views.create_hood, name='create_hood'),
]