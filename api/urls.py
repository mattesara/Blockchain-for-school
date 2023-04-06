from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('degree/list', views.degree_list, name='degree_list'),
    path('search/result', views.search_result, name='search_result'),
    path('degree/<int:pk>/', views.degree_detail, name='degree_detail'),
    path('degree/new/', views.degree_new, name='degree_new'),
    path('degree/<int:pk>/edit/', views.degree_edit, name='degree_edit'),

]
