# -*- coding: utf-8 -*-
from django.conf.urls import url

from mano_id import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]
