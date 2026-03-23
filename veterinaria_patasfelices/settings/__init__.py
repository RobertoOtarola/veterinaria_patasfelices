import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("DJANGO_ENV", "development")

if ENV == "production":
    from .production import *
else:
    from .development import *
