"""
Management command to create the 'asistente_clinica' user
and 'Editores Fichas' group with the correct permissions
as specified in practica_clase_10.md (Pasos 9-10).

Usage:
    python manage.py crear_editor
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from fichas.models import Dueno, Mascota, ConsultaMedica


class Command(BaseCommand):
    help = "Crea el usuario 'asistente_clinica' y el grupo 'Editores Fichas'"

    def handle(self, *args, **options):
        # --- Grupo ---
        group, created = Group.objects.get_or_create(name="Editores Fichas")
        if created:
            self.stdout.write(self.style.SUCCESS("Grupo 'Editores Fichas' creado."))
        else:
            self.stdout.write("Grupo 'Editores Fichas' ya existe.")

        # Permisos del grupo (sin delete)
        perms_map = {
            Dueno: ['view_dueno', 'change_dueno'],
            Mascota: ['view_mascota', 'add_mascota', 'change_mascota'],
            ConsultaMedica: ['view_consultamedica', 'add_consultamedica', 'change_consultamedica'],
        }

        for model, codenames in perms_map.items():
            ct = ContentType.objects.get_for_model(model)
            for codename in codenames:
                perm = Permission.objects.get(content_type=ct, codename=codename)
                group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS("Permisos asignados al grupo."))

        # --- Usuario ---
        if User.objects.filter(username='asistente_clinica').exists():
            self.stdout.write("Usuario 'asistente_clinica' ya existe.")
        else:
            user = User.objects.create_user(
                username='asistente_clinica',
                password='PatasFelices2024!',
                is_staff=True,
                is_superuser=False,
            )
            user.groups.add(group)
            self.stdout.write(self.style.SUCCESS(
                "Usuario 'asistente_clinica' creado (password: PatasFelices2024!)."
            ))

        self.stdout.write(self.style.SUCCESS("\n✅ Todo listo. Pasos 9-10 completados."))
