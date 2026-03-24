# 🐾 Veterinaria "PatasFelices"

Aplicación web desarrollada con Django para la gestión de dueños, mascotas y consultas médicas en una clínica veterinaria ficticia. Permite realizar operaciones CRUD completas desde el navegador.

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
* Modelo registrado con motivo, diagnóstico, tratamiento y costo
* Listado visible desde el detalle de cada mascota
* Gestión vía panel de administración

### 🔗 Relaciones
* **Dueño → Mascotas** (1:N)
* **Mascota → Consultas Médicas** (1:N)

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

### 6. Ejecutar servidor

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
│   ├── views.py                        # 10 CBVs + HomeView
│   ├── urls.py                         # 10 rutas CRUD + inicio
│   ├── admin.py                        # 3 modelos registrados
│   ├── apps.py
│   ├── tests.py
│   └── migrations/
└── templates/
    └── fichas/
        ├── base.html                   # Template base con nav y CSS
        ├── inicio.html                 # Página de inicio
        ├── dueno_list.html             # Tabla de dueños
        ├── dueno_detail.html           # Detalle + mascotas asociadas
        ├── dueno_form.html             # Crear/editar dueño
        ├── dueno_confirm_delete.html   # Confirmación de eliminación
        ├── mascota_list.html           # Tabla de mascotas
        ├── mascota_detail.html         # Detalle + consultas médicas
        ├── mascota_form.html           # Crear/editar mascota
        └── mascota_confirm_delete.html # Confirmación de eliminación
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

---

## 🔮 Mejoras futuras

* 🔐 Sistema de autenticación de usuarios
* 📊 Dashboard con métricas avanzadas
* 🐳 Dockerización del proyecto
* 🌐 API REST con Django REST Framework
* ✅ Tests unitarios y de integración

---

## 👨‍💻 Autor

**Roberto Otárola**

* GitHub: [RobertoOtarola](https://github.com/RobertoOtarola)

---

## 📄 Licencia

GPL-3.0

