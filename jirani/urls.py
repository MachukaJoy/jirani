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
  path('hoods/', views.hoods, name='hoods'),
  path('hood/<hood_id>', views.hood, name='hood'),
  path('join-hood/<id>', views.join_hood, name='join_hood'),
  path('leave-hood/<id>', views.leave_hood, name='leave_hood'),
  path('occupants/<hood_id>', views.hood_occupants, name='occupants'),
]