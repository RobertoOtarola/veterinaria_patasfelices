from django.urls import path
from . import views

app_name = 'fichas'

urlpatterns = [
    # HOME
    path('', views.inicio, name='inicio'),

    # ===== DUEÑOS =====
    path('duenos/', views.DuenoListView.as_view(), name='dueno_lista'),
    path('duenos/<int:pk>/', views.DuenoDetailView.as_view(), name='dueno_detalle'),
    path('duenos/nuevo/', views.DuenoCreateView.as_view(), name='dueno_crear'),
    path('duenos/editar/<int:pk>/', views.DuenoUpdateView.as_view(), name='dueno_editar'),
    path('duenos/eliminar/<int:pk>/', views.DuenoDeleteView.as_view(), name='dueno_eliminar'),

    # ===== MASCOTAS =====
    path('mascotas/', views.MascotaListView.as_view(), name='mascota_lista'),
    path('mascotas/<int:pk>/', views.MascotaDetailView.as_view(), name='mascota_detalle'),
    path('mascotas/nuevo/', views.MascotaCreateView.as_view(), name='mascota_crear'),
    path('mascotas/editar/<int:pk>/', views.MascotaUpdateView.as_view(), name='mascota_editar'),
    path('mascotas/eliminar/<int:pk>/', views.MascotaDeleteView.as_view(), name='mascota_eliminar'),

    # ===== CONSULTAS MÉDICAS =====
    path('consultas/', views.ConsultaListView.as_view(), name='consulta_lista'),
    path('consultas/<int:pk>/', views.ConsultaDetailView.as_view(), name='consulta_detalle'),
    path('consultas/nuevo/', views.ConsultaCreateView.as_view(), name='consulta_crear'),
    path('consultas/editar/<int:pk>/', views.ConsultaUpdateView.as_view(), name='consulta_editar'),
    path('consultas/eliminar/<int:pk>/', views.ConsultaDeleteView.as_view(), name='consulta_eliminar'),
]
