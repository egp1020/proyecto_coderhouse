from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from estudiante.models import Estudiante


class ListadoEstudiantes(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = 'estudiante/listar_estudiante.html'


class CrearEstudiante(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Estudiante
    permission_required = "estudiante.add_estudiante"
    template_name = 'estudiante/crear_estudiante.html'
    success_url = reverse_lazy('listado_estudiantes')
    fields = '__all__'


class EditarEstudiante(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Estudiante
    permission_required = "estudiante.change_estudiante"
    template_name = 'estudiante/editar_estudiante.html'
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('mostrar_estudiante', kwargs={'pk':self.object.pk})


class EliminarEstudiante(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Estudiante
    permission_required = "estudiante.delete_estudiante"
    template_name = 'estudiante/eliminar_estudiante.html'
    success_url = reverse_lazy('listado_estudiantes')

class MostrarEstudiante(LoginRequiredMixin, DetailView):
    model = Estudiante
    template_name = 'estudiante/mostrar_estudiante.html'
