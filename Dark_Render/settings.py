import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g=ls0puqesdcq(8ts3%e()9o&0vrx)g@!!hijnauf#9n!(s!21v'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if not DEBUG:
    PREPEND_WWW = False
    BASE_URL = "https://dark-render.com"

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['https://dark-render.com','https://www.dark-render.com','www.dark-render.com','dark-render.com']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


if not DEBUG:
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = "DENY"
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True


ROOT_URLCONF = 'Dark_Render.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Dark_Render.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'uk-uk'

LANGUAGES = (
    ('uk', 'Ukrainian'),
    ('en', 'English'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

if not DEBUG:
    STATIC_ROOT = '/home3/darkrend/public_html/static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
if not DEBUG:
    MEDIA_ROOT = '/home3/darkrend/public_html/media'
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# TinyMCE
TINYMCE_JS_URL = os.path.join("", "js/tinymce/tinymce.min.js")
TINYMCE_JS_ROOT = os.path.join("", "js/tinymce")
TINYMCE_DEFAULT_CONFIG = {
    'height': 400,
    'width': 1120,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea#id_mce_description',
    'theme': 'silver',
    'plugins': '''
            textcolor,save,link,image,media,preview,codesample,contextmenu,
            table,code,lists,fullscreen,insertdatetime,nonbreaking,
            contextmenu,directionality,searchreplace,wordcount,visualblocks,
            visualchars,code,fullscreen,autolink,lists,charmap,print,hr,
            anchor,pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}

# EMAIL config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

GOOGLE_RECAPTCHA_SECRET_KEY = '6Ldtld4UAAAAAEG1XoqH6NjDqzigt6L5ZXwT_GYR'

EMAIL_USE_SSL = True
EMAIL_HOST = 'dark-render.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'noreply@dark-render.com'
EMAIL_HOST_PASSWORD = 'Falkonest981'
