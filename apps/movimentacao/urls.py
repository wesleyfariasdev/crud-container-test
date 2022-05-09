from django.urls import path
from . import views

app_name = 'movement'
urlpatterns = [
    path('', views.movement_list, name='list'),
    path('create/new/movement/', views.MovementCreate.as_view(), name='create_movement'),
    path('update/movement/<int:pk>/', views.MovementUpdate.as_view(), name='update_movement'),
    path('delete/movement/<int:pk>/', views.delete_movement, name='delete_movement'),

]
