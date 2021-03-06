from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    url(r'^search/$', views.search, name='search'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^project/$', views.project, name='project'),
]
