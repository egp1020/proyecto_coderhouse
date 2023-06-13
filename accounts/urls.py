from django.urls import path
from accounts import views


urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('perfil/', views.mostrar_perfil, name='mostrar_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/cambiar-password/', views.CambiarPassword.as_view(), name='cambiar_password'),
    path('perfil/eliminar/<int:pk>/', views.EliminarPerfil.as_view(), name='eliminar_perfil'),
]