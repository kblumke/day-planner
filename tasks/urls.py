from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<day_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^new/$', views.add_day, name='new_day'),
    url(r'^(?P<day_id>[0-9]+)/edit/$', views.edit_day, name='edit_day')
]