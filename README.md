# 🐾 Veterinaria "PatasFelices"

Aplicación web desarrollada con Django para la gestión de dueños, mascotas y consultas médicas en una clínica veterinaria ficticia. Incluye CRUD completo, panel de administración personalizado y sistema de permisos por roles.

---

## 🚀 Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| **Django 6.0** | Backend y templates |
| **SQLite** | Base de datos en desarrollo |
| **PostgreSQL (Supabase)** | Base de datos en producción |
| **python-dotenv** | Variables de entorno |
| **dj-database-url** | Configuración de BD por URL |
| **Git + GitHub** | Control de versiones |

---

## 📌 Funcionalidades principales

### 🧑‍⚕️ Dueños
* Crear, listar, ver detalle, editar y eliminar dueños
* Ver mascotas asociadas desde el detalle

### 🐶 Mascotas
* Crear, listar, ver detalle, editar y eliminar mascotas
* Seleccionar dueño desde dropdown
* Ver consultas médicas desde el detalle

### 🏥 Consultas Médicas
* CRUD completo con vistas y templates
* Listado visible desde el detalle de cada mascota
* Gestión vía panel de administración

### 🔗 Relaciones
* **Dueño → Mascotas** (1:N)
* **Mascota → Consultas Médicas** (1:N)

### 🛡️ Admin Personalizado
* Inlines: mascotas dentro del dueño, consultas dentro de la mascota
* Columnas calculadas: cantidad de mascotas, costo total de consultas
* Acciones masivas: marcar consultas sin costo, exportar dueños
* Branding "PatasFelices" en el panel

### 🔐 Permisos y Seguridad
* Vistas de eliminación protegidas con `PermissionRequiredMixin`
* Usuario `asistente_clinica` con rol de editor (sin delete)
* Grupo `Editores Fichas` con permisos reutilizables
* Página 403 personalizada

---

## 🛠️ Instalación y ejecución

### 1. Clonar repositorio

```bash
git clone https://github.com/RobertoOtarola/veterinaria_patasfelices.git
cd veterinaria_patasfelices
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Copiar el archivo de ejemplo y completar los valores:

```bash
cp .env.example .env
```

Variables requeridas:

```env
DJANGO_ENV=development
SECRET_KEY=tu-clave-secreta
DEBUG=True
DATABASE_URL=postgres://user:password@host:port/dbname
```

### 5. Aplicar migraciones y crear superusuario

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Crear usuario editor y grupo de permisos

```bash
python manage.py crear_editor
```

Esto crea el usuario `asistente_clinica` y el grupo `Editores Fichas` automáticamente.

### 7. Ejecutar servidor

```bash
python manage.py runserver
```

Acceder a: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📁 Estructura del proyecto

```
veterinaria_patasfelices/
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
├── veterinaria_patasfelices/           # Configuración del proyecto
│   ├── __init__.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── settings/
│       ├── __init__.py                 # Selecciona entorno (dev/prod)
│       ├── base.py                     # Configuración compartida
│       ├── development.py              # SQLite, DEBUG=True
│       └── production.py               # PostgreSQL (Supabase), DEBUG=False
├── fichas/                             # App principal
│   ├── __init__.py
│   ├── models.py                       # Dueno, Mascota, ConsultaMedica
│   ├── views.py                        # 15 CBVs + inicio (con permisos)
│   ├── urls.py                         # 15 rutas CRUD + inicio
│   ├── admin.py                        # Admin personalizado con inlines y acciones
│   ├── apps.py
│   ├── tests.py
│   ├── migrations/
│   └── management/
│       └── commands/
│           └── crear_editor.py         # Crea usuario y grupo de permisos
└── templates/
    ├── 403.html                        # Página de error personalizada
    └── fichas/
        ├── base.html                   # Template base con nav y CSS
        ├── inicio.html                 # Dashboard con contadores
        ├── dueno_list.html             # Tabla con búsqueda y paginación
        ├── dueno_detail.html           # Detalle + mascotas asociadas
        ├── dueno_form.html             # Crear/editar dueño
        ├── dueno_confirm_delete.html   # Confirmación de eliminación
        ├── mascota_list.html           # Tabla con paginación
        ├── mascota_detail.html         # Detalle + consultas médicas
        ├── mascota_form.html           # Crear/editar mascota
        ├── mascota_confirm_delete.html # Confirmación de eliminación
        ├── consultamedica_list.html    # Tabla de consultas
        ├── consultamedica_detail.html  # Detalle de consulta
        ├── consultamedica_form.html    # Crear/editar consulta
        └── consultamedica_confirm_delete.html
```

---

## 🧠 Conceptos aplicados

* Arquitectura **MVT (Model-View-Template)**
* Class-Based Views (ListView, DetailView, CreateView, UpdateView, DeleteView)
* ORM de Django con relaciones ForeignKey (1:N)
* Template inheritance (`base.html`)
* Protección CSRF en formularios
* Separación de settings por entorno (`base`, `development`, `production`)
* Variables de entorno con `.env` y `python-dotenv`
* Admin personalizado con `ModelAdmin`, inlines, acciones y columnas calculadas
* Sistema de permisos con `LoginRequiredMixin` y `PermissionRequiredMixin`
* Grupos y roles de usuario (`Editores Fichas`)
* Management commands personalizados (`crear_editor`)
* Paginación y búsqueda en vistas de lista
* Mensajes de éxito con `SuccessMessageMixin`
* Validación de RUT con `clean()` en el modelo

---

## 🔮 Mejoras futuras

* 🐳 Dockerización del proyecto
* 🌐 API REST con Django REST Framework
* ✅ Tests unitarios y de integración
* 📧 Notificaciones por email
* 📈 Reportes exportables (CSV/PDF)

---

## 👨‍💻 Autor

**Roberto Otárola**

* GitHub: [RobertoOtarola](https://github.com/RobertoOtarola)

---

## 📄 Licencia

GPL-3.0

