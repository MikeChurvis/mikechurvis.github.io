from portfolio.settings.common import *

DEBUG = True

SECRET_KEY = 'insecure-debug-secret-key-12345'

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', '[::1]']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}

CORS_ALLOWED_ORIGINS = ['http://localhost:3000']

CONTACT_FORM_NAME_MAXLENGTH = 120
CONTACT_FORM_COMPANY_MAXLENGTH = 180
CONTACT_FORM_EMAIL_MAXLENGTH = 320
CONTACT_FORM_EMAIL_REGEX = "^([a-zA-Z0-9_+-]+\.)*[a-zA-Z0-9_+-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]+$"
CONTACT_FORM_MESSAGE_CONTENT_MAXLENGTH = 1000
CONTACT_FORM_MESSAGE_CONTENT_MINLENGTH = 20
