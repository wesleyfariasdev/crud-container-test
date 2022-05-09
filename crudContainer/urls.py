from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.cliente.urls', namespace='client')),
    path('container/', include('apps.container.urls', namespace='container')),
    path('movimentacao/', include('apps.movimentacao.urls', namespace='movimentacao')),
]
