import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "os9n89@w-cb&v%h1843f(a(b1fu^si!hqn@)0k1ulxh$*l))t5"
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ["dreambamboohouse.com.np", "www.dreambamboohouse.com.np"]


INSTALLED_APPS = [
    "users",
    "consultancydocs",
    "tailwind",
    "student",
    "theme",
    "qr_code",
    "django_browser_reload",
    "django_cleanup.apps.CleanupConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "users.context.consultancy",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

INTERNAL_IPS = [
    "127.0.0.1",
]

WSGI_APPLICATION = "core.wsgi.application"


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "dreambam_consultancy_docs",
#         "USER": "dreambam_pokhrelgopal",
#         "PASSWORD": "pokhrelgopal",
#         "HOST": "localhost",
#         "PORT": "",
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

TAILWIND_APP_NAME = "theme"

AUTH_USER_MODEL = "users.User"

BUNNY_STORAGE_ZONE_NAME = "agentdocx"
BUNNY_PULL_ZONE_URL = "AgentDocxPullZone.b-cdn.net"
BUNNY_API_KEY = "01c261fd-a0e0-41bd-878c95b96c17-0079-45a2"
BUNNY_STORAGE_ZONE_REGION = "SG"
