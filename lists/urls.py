from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('new', views.new_list, name='new_list'),
    path('<int:list_id>/', views.view_list, name='view_list'),
    path('<int:list_id>/share', views.share_list, name='share_list'),
    path('users/<str:email>/', views.my_lists, name='my_lists'),
]


