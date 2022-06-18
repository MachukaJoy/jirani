from django.conf.urls import url
from . import views

urlpatterns = [
  url('^$', views.jiranitest, name='welcome'),
  url('^today/$',views.news_of_day, name ='newsToday')
]