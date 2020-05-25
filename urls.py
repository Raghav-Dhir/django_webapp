from django.conf.urls import url
from SecondApp import views

urlpatterns = [
    url(r'^$', views.users, name='users'),

]