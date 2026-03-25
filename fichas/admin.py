from django.contrib import admin
from django.db.models import Sum
from .models import Dueno, Mascota, ConsultaMedica


# ===== INLINES =====

class MascotaInline(admin.TabularInline):
    model = Mascota
    extra = 1
    fields = ('nombre', 'especie', 'raza', 'fecha_nacimiento')


class ConsultaMedicaInline(admin.TabularInline):
    model = ConsultaMedica
    extra = 1
    fields = ('motivo', 'diagnostico', 'tratamiento', 'costo', 'fecha')
    readonly_fields = ('fecha',)


# ===== MODEL ADMINS =====

@admin.register(Dueno)
class DuenoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'telefono', 'email', 'cantidad_mascotas')
    search_fields = ('nombre', 'rut')
    ordering = ['nombre']
    inlines = [MascotaInline]
    actions = ['exportar_seleccionados']

    # Paso 8 — Columna calculada
    def cantidad_mascotas(self, obj):
        return obj.mascota_set.count()
    cantidad_mascotas.short_description = "Mascotas"

    # Paso 6 — Acción: exportar dueños seleccionados
    def exportar_seleccionados(self, request, queryset):
        nombres = ", ".join(
            f"{d.nombre} ({d.rut})" for d in queryset
        )
        self.message_user(
            request,
            f"Dueños seleccionados: {nombres}"
        )
    exportar_seleccionados.short_description = "Exportar dueños seleccionados (texto)"


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'dueno', 'costo_total_consultas')
    search_fields = ('nombre', 'dueno__nombre')
    list_filter = ('especie',)
    ordering = ['nombre']
    inlines = [ConsultaMedicaInline]

    # Paso 8 — Columna calculada
    def costo_total_consultas(self, obj):
        total = obj.consultamedica_set.aggregate(
            total=Sum('costo')
        )['total']
        if total is not None:
            return f"${total:,.0f}"
        return "$0"
    costo_total_consultas.short_description = "Costo total consultas"


@admin.register(ConsultaMedica)
class ConsultaMedicaAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'motivo', 'fecha', 'costo')
    search_fields = ('motivo', 'mascota__nombre')
    list_filter = ('fecha',)
    ordering = ['-fecha']
    readonly_fields = ('fecha',)
    actions = ['marcar_sin_costo']

    # Paso 6 — Acción: marcar consultas como sin costo
    def marcar_sin_costo(self, request, queryset):
        updated = queryset.update(costo=0)
        self.message_user(
            request,
            f"{updated} consulta(s) actualizada(s) a costo $0."
        )
    marcar_sin_costo.short_description = "Marcar como sin costo"


# ===== BRANDING (Paso 7) =====

admin.site.site_header = "🐾 PatasFelices — Panel de Administración"
admin.site.site_title = "PatasFelices Admin"
admin.site.index_title = "Gestión de Fichas Veterinarias"
