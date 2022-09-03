from django.urls import re_path
from jobs import views
 
urlpatterns = [
    re_path(r'^job/create$', views.create_job),
    re_path(r'^job/get/(?P<pk>[0-9]+)$', views.get_job),
    re_path(r'^job/delete/(?P<pk>[0-9]+)$', views.delete_job),
]