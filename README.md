# 🐾 Clínica Veterinaria "PatasFelices"

Aplicación web desarrollada con Django para la gestión de dueños y mascotas en una clínica veterinaria. Permite administrar registros, visualizar relaciones entre entidades y realizar operaciones CRUD completas.

---

## 🚀 Tecnologías utilizadas

* **Backend:** Django (Python)
* **Base de datos:** SQLite (desarrollo)
* **Frontend:** Django Templates (HTML)
* **Gestión de entorno:** python-dotenv
* **Control de versiones:** Git + GitHub

---

## 📌 Funcionalidades principales

### 🧑‍⚕️ Dueños

* Crear, listar, editar y eliminar dueños
* Visualizar detalle de cada dueño
* Ver mascotas asociadas

### 🐶 Mascotas

* Crear, listar, editar y eliminar mascotas
* Asociar mascotas a dueños
* Visualizar detalle de cada mascota

### 🔗 Relaciones

* Relación **1:N (Dueño → Mascotas)**
* Navegación entre entidades

---

## 📊 Dashboard (Inicio)

* Total de dueños registrados
* Total de mascotas registradas
* Acceso rápido a módulos principales

---

## 🛠️ Instalación y ejecución

### 1. Clonar repositorio

```bash
git clone https://github.com/RobertoOtarola/veterinaria_patasfelices.git
cd veterinaria_patasfelices
```

---

### 2. Crear entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Configurar variables de entorno

Crear archivo `.env` en la raíz:

```env
DJANGO_ENV=development
SECRET_KEY=your_secret_key
DEBUG=True
```

---

### 5. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Ejecutar servidor

```bash
python manage.py runserver
```

Acceder a:

```
http://127.0.0.1:8000/
```

---

## 📁 Estructura del proyecto

```
veterinaria_patasfelices/
├── fichas/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── templates/
│   └── fichas/
├── manage.py
├── requirements.txt
└── .env
```

---

## 🧠 Conceptos aplicados

* Arquitectura **MVT (Model-View-Template)**
* Class-Based Views (CBV)
* ORM de Django
* Relaciones entre modelos (ForeignKey)
* Template inheritance (`base.html`)
* Buenas prácticas con `.env` y configuración

---

## 🔮 Mejoras futuras

* 📅 Módulo de consultas médicas
* 🔐 Sistema de autenticación de usuarios
* 📊 Dashboard con métricas avanzadas
* 🐘 Migración a PostgreSQL
* 🐳 Dockerización del proyecto
* 🌐 API REST con Django REST Framework

---

## 📸 Capturas (opcional)

*Agregar screenshots del sistema en funcionamiento*

---

## 👨‍💻 Autor

**Roberto Otárola**

* GitHub: https://github.com/RobertoOtarola

---

## 📄 Licencia

GPL-3.0

