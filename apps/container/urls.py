from django.urls import path
from . import views

app_name = 'container'
urlpatterns = [
    path('', views.container_list, name='list'),
    path('create/new/container/', views.CreateContainer.as_view(), name='create_container'),
    path('update/container/<int:pk>/', views.UpdateContainer.as_view(), name='update_container'),
    path('delete/container/<int:pk>/', views.delete_container, name='delete_container'),
]
