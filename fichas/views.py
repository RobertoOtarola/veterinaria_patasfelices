from django.urls import reverse_lazy
from django.views.generic import *
from .models import Dueno, Mascota


# ===== DUEÑO =====
class DuenoListView(ListView):
    model = Dueno


class DuenoDetailView(DetailView):
    model = Dueno


class DuenoCreateView(CreateView):
    model = Dueno
    fields = '__all__'
    success_url = reverse_lazy('fichas:dueno_lista')


class DuenoUpdateView(UpdateView):
    model = Dueno
    fields = '__all__'
    success_url = reverse_lazy('fichas:dueno_lista')


class DuenoDeleteView(DeleteView):
    model = Dueno
    success_url = reverse_lazy('fichas:dueno_lista')


# ===== MASCOTA =====
class MascotaListView(ListView):
    model = Mascota


class MascotaDetailView(DetailView):
    model = Mascota


class MascotaCreateView(CreateView):
    model = Mascota
    fields = '__all__'
    success_url = reverse_lazy('fichas:mascota_lista')


class MascotaUpdateView(UpdateView):
    model = Mascota
    fields = '__all__'
    success_url = reverse_lazy('fichas:mascota_lista')


class MascotaDeleteView(DeleteView):
    model = Mascota
    success_url = reverse_lazy('fichas:mascota_lista')
