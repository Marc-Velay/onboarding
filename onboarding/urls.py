from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^doc_scan/$', views.doc_scan, name='doc_scan'),
]

