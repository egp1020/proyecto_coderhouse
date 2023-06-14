from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from profesor.models import Profesor


class ListadoProfesores(ListView):
    model = Profesor
    template_name = 'profesor/listar_profesor.html'


class CrearProfesor(CreateView):
    model = Profesor
    template_name = 'profesor/crear_profesor.html'
    success_url = reverse_lazy('listado_profesores')
    fields = '__all__'


class EditarProfesor(UpdateView):
    model = Profesor
    template_name = 'profesor/editar_profesor.html'
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('mostrar_profesor', kwargs={'pk':self.object.pk})


class EliminarProfesor(DeleteView):
    model = Profesor
    template_name = 'profesor/eliminar_profesor.html'
    success_url = reverse_lazy('listado_profesores')

class MostrarProfesor(DetailView):
    model = Profesor
    template_name = 'profesor/mostrar_profesor.html'


