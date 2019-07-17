from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('get_menu', views.get_menu, name='get_menu'),
    path('get_menu_detail', views.get_menu_detail, name='get_menu_detail'),
]
