from django.urls import path
from . import views

app_name = 'fichas'

urlpatterns = [
    path('duenos/', views.DuenoListView.as_view(), name='dueno_lista'),
    path('duenos/<int:pk>/', views.DuenoDetailView.as_view(), name='dueno_detalle'),
    path('duenos/nuevo/', views.DuenoCreateView.as_view(), name='dueno_crear'),
    path('duenos/editar/<int:pk>/', views.DuenoUpdateView.as_view(), name='dueno_editar'),
    path('duenos/eliminar/<int:pk>/', views.DuenoDeleteView.as_view(), name='dueno_eliminar'),

    path('mascotas/', views.MascotaListView.as_view(), name='mascota_lista'),
    path('mascotas/<int:pk>/', views.MascotaDetailView.as_view(), name='mascota_detalle'),
]
