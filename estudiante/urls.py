from django.urls import path
from estudiante import views


urlpatterns = [
    path('estudiantes/', views.ListadoEstudiantes.as_view(), name='listado_estudiantes'),
    path('crear-estudiante/', views.CrearEstudiante.as_view(), name='crear_estudiante'),
    path('editar-estudiante/<int:pk>/', views.EditarEstudiante.as_view(), name='editar_estudiante'),
    path('eliminar-estudiante/<int:pk>/', views.EliminarEstudiante.as_view(), name='eliminar_estudiante'),
    path('mostrar-estudiante/<int:pk>/', views.MostrarEstudiante.as_view(), name='mostrar_estudiante'),
]