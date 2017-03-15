from django.conf.urls import url

import os

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
