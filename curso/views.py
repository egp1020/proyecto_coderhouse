from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from curso.models import Curso


class ListadoCursos(ListView):
    model = Curso
    template_name = 'curso/listar_curso.html'


class CrearCurso(CreateView):
    model = Curso
    template_name = 'curso/crear_curso.html'
    success_url = reverse_lazy('listado_cursos')
    fields = '__all__'


class EditarCurso(UpdateView):
    model = Curso
    template_name = 'curso/editar_curso.html'
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('mostrar_curso', kwargs={'pk':self.object.pk})


class EliminarCurso(DeleteView):
    model = Curso
    template_name = 'curso/eliminar_curso.html'
    success_url = reverse_lazy('listado_cursos')

class MostrarCurso(DetailView):
    model = Curso
    template_name = 'curso/mostrar_curso.html'

