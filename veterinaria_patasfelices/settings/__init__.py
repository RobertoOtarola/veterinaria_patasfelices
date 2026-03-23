import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_PKG_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = PROJECT_PKG_DIR.parent

# Carga variables desde el `.env` ubicado junto al paquete `veterinaria_patasfelices/`.
# (Si no existe ahí, cae a la raíz del repo por compatibilidad.)
env_path = PROJECT_PKG_DIR / ".env"
if not env_path.exists():
    env_path = REPO_ROOT / ".env"
load_dotenv(dotenv_path=env_path)

ENV = os.getenv("DJANGO_ENV", "development").strip().lower()

if ENV == "production":
    from .production import *
else:
    from .development import *
