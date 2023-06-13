from django.urls import path
from profesor import views


urlpatterns = [
    path('profesores/', views.ListadoProfesores.as_view(), name='listado_profesores'),
    path('crear-profesor/', views.CrearProfesor.as_view(), name='crear_profesor'),
    path('editar-profesor/<int:pk>/', views.EditarProfesor.as_view(), name='editar_profesor'),
    path('eliminar-profesor/<int:pk>/', views.EliminarProfesor.as_view(), name='eliminar_profesor'),
    path('mostrar-profesor/<int:pk>/', views.MostrarProfesor.as_view(), name='mostrar_profesor'),
]
