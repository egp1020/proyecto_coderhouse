from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from estudiante.models import Estudiante


class ListadoEstudiantes(ListView):
    model = Estudiante
    template_name = 'estudiante/listar_estudiante.html'


class CrearEstudiante(CreateView):
    model = Estudiante
    template_name = 'estudiante/crear_estudiante.html'
    success_url = reverse_lazy('listado_estudiantes')
    fields = '__all__'


class EditarEstudiante(UpdateView):
    model = Estudiante
    template_name = 'estudiante/editar_estudiante.html'
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('mostrar_estudiante', kwargs={'pk':self.object.pk})


class EliminarEstudiante(DeleteView):
    model = Estudiante
    template_name = 'estudiante/eliminar_estudiante.html'
    success_url = reverse_lazy('listado_estudiantes')

class MostrarEstudiante(DetailView):
    model = Estudiante
    template_name = 'estudiante/mostrar_estudiante.html'
