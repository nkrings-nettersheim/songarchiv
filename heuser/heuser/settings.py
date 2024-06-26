"""
Django settings for heuser project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

#from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "4kq1sj_c6j"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.bheuser-songarchiv.de', 'bheuser-songarchiv.de']

# Application definition

INSTALLED_APPS = [
    #'songarchiv.apps.SongarchivConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_ckeditor_5',
    'cookiebanner',
    'django_user_agents',
    'songarchiv',
    'dashboard',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


ROOT_URLCONF = 'heuser.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'songarchiv.context_processors.setting_enhancement',
            ],
        },
    },
]


WSGI_APPLICATION = 'heuser.wsgi.application'


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


# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/songarchiv/'
LOGOUT_REDIRECT_URL = '/songarchiv/'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

#USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#MEDIA_ROOT = os.path.join(BASE_DIR, 'songarchiv/static/songarchiv/mp3/')


####################################
## cookiebanner configuration
####################################
COOKIEBANNER = {
    "title": ("Cookie Einstellungen"),
    "header_text": ("Wir nutzen zum einen Cookies die für den Betrieb der Webseite unumgänglich sind. "
                     "Weiterhin setzen wie Open Web Analytics zur Verbesserung der Nutzererfahrung auf der Webseite ein. <br>"
                     "Weitere Informationen finden sie in den Datenschutzbestimmungen"),
    "footer_text": ("Bitte Cookies akzeptieren:"),
    "footer_links": [
        {
            "title": ("Impressum"),
            "href": "/songarchiv/impressum"
        },
        {
            "title": ("Datenschutz"),
            "href": "/songarchiv/datenschutz"
        },
    ],
    "groups": [
        {
            "id": "essential",
            "name": ("Essential"),
            "description": ("Essentielle cookies erlauben die Funktion der Website."),
            "cookies": [
                {
                    "pattern": "cookiebanner",
                    "description": ("Damit dieser Hinweis nur beim ersten Aufruf erfolgt."),
                },
                {
                    "pattern": "csrftoken",
                    "description": ("Cookie hilft Cross-Site-Request-Forgery Attacken zu verhindern."),
                },
            ],
        },
        {
            "id": "analytics",
            "name": ("Analytics"),
            "optional": True,
            "cookies": [
                {
                    "pattern": "_owa_.*",
                    "description": ("Open Web Analytics Cookies zur Website Analysis. Weitere Information in der Datenschutzerklärung"),
                },
            ],
        },
    ],
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

####################################
##  CKEDITOR CONFIGURATION ##
####################################

#from ckeditor.configs import DEFAULT_CONFIG

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {'default':
                        {'height': 160,
                         'defaultLanguage': "de",
                         'scayt_autoStartup': True,
                         'scayt_sLang': "de_DE",
                         'coreStyles_bold': {'element': 'b', 'overrides': 'strong'},
                         'coreStyles_italic': {'element': 'i', 'overrides': 'em'},
                         'toolbar': 'Custom', 'toolbar_Custom':
                             [
                                 ['Format', 'Bold', 'Italic', 'Underline', 'BGColor', 'TextColor', 'Link', 'Scayt', ],
                             ],
                         },
                    'text':
                        {'height': 380,
                         'width': 800,
                         'defaultLanguage': "de",
                         'scayt_autoStartup': True,
                         'scayt_sLang': "de_DE",
                         'coreStyles_bold': {'element': 'b', 'overrides': 'strong'},
                         'coreStyles_italic': {'element': 'i', 'overrides': 'em'},
                         'toolbar': 'Custom', 'toolbar_Custom':
                             [
                                 ['Bold', 'Italic', 'Underline', 'BGColor', 'TextColor'],
                                 {'name': 'styles', 'items': ['Font', 'FontSize']},
                             ],
                         },
                    'chords':
                        {'height': 380,
                         'width': 800,
                         'defaultLanguage': "de",
                         'scayt_autoStartup': True,
                         'scayt_sLang': "de_DE",
                         'coreStyles_bold': {'element': 'b', 'overrides': 'strong'},
                         'coreStyles_italic': {'element': 'i', 'overrides': 'em'},
                         'toolbar': 'Custom', 'toolbar_Custom':
                             [
                                 ['Bold', 'Italic', 'Underline', 'BGColor', 'TextColor'],
                                 {'name': 'styles', 'items': ['Font', 'FontSize']},
                             ],
                         }
                    }

###################################


###################################
##  neue CKEditor 5 config       ##
###################################

customColorPalette = [
    {
        'color': 'hsl(4, 90%, 58%)',
        'label': 'Red'
    },
    {
        'color': 'hsl(340, 82%, 52%)',
        'label': 'Pink'
    },
    {
        'color': 'hsl(291, 64%, 42%)',
        'label': 'Purple'
    },
    {
        'color': 'hsl(262, 52%, 47%)',
        'label': 'Deep Purple'
    },
    {
        'color': 'hsl(231, 48%, 48%)',
        'label': 'Indigo'
    },
    {
        'color': 'hsl(207, 90%, 54%)',
        'label': 'Blue'
    },
]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],

    },
    'text': {
        'toolbar': ['bold', 'italic', 'underline', '|', 'fontSize', 'fontFamily', ],
        'language': 'de',
    },
    'chords':
        {
            'toolbar': ['bold', 'italic', 'underline', '|', 'fontSize', 'fontFamily', ],
            'language': 'de',
        },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
        'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                    'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable',],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
            'tableProperties', 'tableCellProperties' ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}


# This must be the last part of the settings file

try:
    from .local_settings import *
except ImportError:
    print('There is no local settings, you must be on production')


