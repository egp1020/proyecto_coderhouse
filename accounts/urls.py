from django.urls import path
from accounts import views


urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('editar-perfil/<int:pk>/', views.editar_perfil, name='editar_perfil'),
    path('eliminar-perfil/<int:pk>/', views.eliminar_perfil, name='eliminar_perfil'),
    path('mostrar-perfil/<int:pk>/', views.mostrar_perfil, name='mostrar_perfil'),
]