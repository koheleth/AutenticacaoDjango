from django.urls import path
from .views import registrar_usuario

urlpatterns = [
    path('registrar_usuario', registrar_usuario, name='registar_usuario'),
]
