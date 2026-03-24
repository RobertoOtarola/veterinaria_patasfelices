from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render
from django.db.models import Q

from .models import Dueno, Mascota, ConsultaMedica


# ===== INICIO (Bonus 2) =====
def inicio(request):
    context = {
        'total_duenos': Dueno.objects.count(),
        'total_mascotas': Mascota.objects.count(),
        'total_consultas': ConsultaMedica.objects.count(),
    }
    return render(request, 'fichas/inicio.html', context)


# ===== DUEÑO =====
class DuenoListView(ListView):
    model = Dueno
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            queryset = queryset.filter(
                Q(nombre__icontains=q) | Q(rut__icontains=q)
            )
        return queryset


class DuenoDetailView(DetailView):
    model = Dueno


class DuenoCreateView(SuccessMessageMixin, CreateView):
    model = Dueno
    fields = '__all__'
    success_url = reverse_lazy('fichas:dueno_lista')
    success_message = "Dueño creado exitosamente."


class DuenoUpdateView(SuccessMessageMixin, UpdateView):
    model = Dueno
    fields = '__all__'
    success_url = reverse_lazy('fichas:dueno_lista')
    success_message = "Dueño actualizado exitosamente."


class DuenoDeleteView(DeleteView):
    model = Dueno
    success_url = reverse_lazy('fichas:dueno_lista')

    def post(self, request, *args, **kwargs):
        messages.success(request, "Dueño eliminado exitosamente.")
        return super().post(request, *args, **kwargs)


# ===== MASCOTA =====
class MascotaListView(ListView):
    model = Mascota
    paginate_by = 10


class MascotaDetailView(DetailView):
    model = Mascota


class MascotaCreateView(SuccessMessageMixin, CreateView):
    model = Mascota
    fields = '__all__'
    success_url = reverse_lazy('fichas:mascota_lista')
    success_message = "Mascota creada exitosamente."


class MascotaUpdateView(SuccessMessageMixin, UpdateView):
    model = Mascota
    fields = '__all__'
    success_url = reverse_lazy('fichas:mascota_lista')
    success_message = "Mascota actualizada exitosamente."


class MascotaDeleteView(DeleteView):
    model = Mascota
    success_url = reverse_lazy('fichas:mascota_lista')

    def post(self, request, *args, **kwargs):
        messages.success(request, "Mascota eliminada exitosamente.")
        return super().post(request, *args, **kwargs)


# ===== CONSULTA MÉDICA (Bonus 1) =====
class ConsultaListView(ListView):
    model = ConsultaMedica
    paginate_by = 10


class ConsultaDetailView(DetailView):
    model = ConsultaMedica


class ConsultaCreateView(SuccessMessageMixin, CreateView):
    model = ConsultaMedica
    fields = '__all__'
    success_url = reverse_lazy('fichas:consulta_lista')
    success_message = "Consulta médica creada exitosamente."


class ConsultaUpdateView(SuccessMessageMixin, UpdateView):
    model = ConsultaMedica
    fields = ['motivo', 'diagnostico', 'tratamiento', 'costo']
    success_url = reverse_lazy('fichas:consulta_lista')
    success_message = "Consulta médica actualizada exitosamente."


class ConsultaDeleteView(DeleteView):
    model = ConsultaMedica
    success_url = reverse_lazy('fichas:consulta_lista')

    def post(self, request, *args, **kwargs):
        messages.success(request, "Consulta médica eliminada exitosamente.")
        return super().post(request, *args, **kwargs)
