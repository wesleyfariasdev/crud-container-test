from django.urls import path
from . import views

app_name = 'client'
urlpatterns = [
    path('', views.client_list, name='list'),
    path('create/new/client/', views.ClientCreate.as_view(), name='create_client'),
    path('update/client/<int:pk>/', views.ClientUpdate.as_view(), name='update_client'),
    path('delete/<int:pk>/', views.delete_client, name='delete_client'),
    path('report/<int:pk>/', views.report_client, name='report'),
    path('search', views.search, name='search'),
]
