from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.table_of_universeties, name='table_of_universeties')
]