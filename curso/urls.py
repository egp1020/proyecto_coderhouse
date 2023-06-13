from django.urls import path
from curso import views


urlpatterns = [
    path('cursos/', views.ListadoCursos.as_view(), name='listado_cursos'),
    path('crear-curso/', views.CrearCurso.as_view(), name='crear_curso'),
    path('editar-curso/<int:pk>/', views.EditarCurso.as_view(), name='editar_curso'),
    path('eliminar-curso/<int:pk>/', views.EliminarCurso.as_view(), name='eliminar_curso'),
    path('mostrar-curso/<int:pk>/', views.MostrarCurso.as_view(), name='mostrar_curso'),
]