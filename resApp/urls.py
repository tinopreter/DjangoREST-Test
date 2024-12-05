from django.urls import path, re_path
from resApp import views

urlpatterns = [
    path('api/v1/users', views.users_list, name='User List'),
    re_path(r'^api/v1/users/(?P<pk>[0-9]+)$', views.users_details, name='User Details')
]