import os
from configurations import Configuration, values

from kubeportal.secret import get_secret_key


class Common(Configuration):
    SECRET_KEY = get_secret_key()

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_extensions',
        'oauth2_provider',
        'oidc_provider',
        'social_django',
        'rest_framework',
        'rest_framework.authtoken',
        'kubeportal',
    ]

    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'kubeportal.middleware.AuthExceptionMiddleware'
    ]

    ROOT_URLCONF = 'kubeportal.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'social_django.context_processors.backends',
                    'social_django.context_processors.login_redirect',
                ],
            },
        },
    ]

    REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': [
                'rest_framework.authentication.TokenAuthentication',
                ],
            'DEFAULT_PERMISSION_CLASSES': [
                'rest_framework.permissions.IsAuthenticated',
                ]
            }

    WSGI_APPLICATION = 'kubeportal.wsgi.application'

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

    AUTHENTICATION_BACKENDS = (
        'social_core.backends.username.UsernameAuth',
        'django.contrib.auth.backends.ModelBackend',
        'social_core.backends.twitter.TwitterOAuth',
        'social_core.backends.google.GoogleOAuth2'
    )

    SOCIAL_AUTH_PIPELINE = (
        'kubeportal.active_directory.user_password',
        'social_core.pipeline.social_auth.social_details',
        'social_core.pipeline.social_auth.social_uid',
        'social_core.pipeline.social_auth.auth_allowed',
        'social_core.pipeline.social_auth.social_user',
        'social_core.pipeline.user.get_username',
        'social_core.pipeline.user.create_user',
        'social_core.pipeline.social_auth.associate_user',
        'social_core.pipeline.social_auth.associate_user',
        'social_core.pipeline.social_auth.load_extra_data',
        'social_core.pipeline.user.user_details',
    )

    SOCIAL_AUTH_USERNAME_FORM_URL = '/login-form/'
    SOCIAL_AUTH_USERNAME_FORM_HTML = 'login_form.html'
    SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/welcome'
    LOGIN_REDIRECT_URL = '/welcome'
    SOCIAL_AUTH_LOGIN_ERROR_URL = '/'
    LOGIN_ERROR_URL = '/'
    LOGIN_URL = '/'
    LOGOUT_REDIRECT_URL = 'index'
    STATIC_URL = '/static/'

    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    CORS_ORIGIN_ALLOW_ALL = True

    ALLOWED_HOSTS = ['*']

    AUTH_USER_MODEL = 'kubeportal.User'
    SOCIAL_AUTH_USER_MODEL = 'kubeportal.User'

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue'
            },
        },
        'formatters': {
            'verbose': {
                'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s"
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false', ],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler'
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins', 'console'],
                'level': 'ERROR',
                'propagate': True,
            },
            'KubePortal': {
                'handlers': ['console', ],
                'level': 'DEBUG',
                'propagate': True,
            },
            'social': {
                'handlers': ['console', ],
                'level': 'DEBUG',
                'propagate': True,
            },
        }
    }

    OIDC_USERINFO = 'kubeportal.oidc.userinfo'
    OIDC_TEMPLATES = {
        'authorize': 'oidc_authorize.html',
        'error': 'oidc_error.html'
    }
    OIDC_IDTOKEN_INCLUDE_CLAIMS = True  # include user email etc. in token
    SESSION_COOKIE_DOMAIN = values.Value(None, environ_prefix='KUBEPORTAL')
    NAMESPACE_CLUSTERROLES = values.ListValue([], environ_prefix='KUBEPORTAL')

    SOCIAL_AUTH_TWITTER_KEY = values.Value(
        None, environ_name='AUTH_TWITTER_KEY', environ_prefix='KUBEPORTAL')
    SOCIAL_AUTH_TWITTER_SECRET = values.Value(
        None, environ_name='AUTH_TWITTER_SECRET', environ_prefix='KUBEPORTAL')
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = values.Value(
        None, environ_name='AUTH_GOOGLE_KEY', environ_prefix='KUBEPORTAL')
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = values.Value(
        None, environ_name='AUTH_GOOGLE_SECRET', environ_prefix='KUBEPORTAL')
    AUTH_AD_DOMAIN = values.Value(None, environ_prefix='KUBEPORTAL')
    AUTH_AD_SERVER = values.Value(None, environ_prefix='KUBEPORTAL')
    SOCIAL_AUTH_SANITIZE_REDIRECTS = False   # let Django handle this

    BRANDING = values.Value('KubePortal', environ_prefix='KUBEPORTAL')
    LANGUAGE_CODE = values.Value('en-us', environ_prefix='KUBEPORTAL')
    TIME_ZONE = values.Value('UTC', environ_prefix='KUBEPORTAL')

    ADMIN_NAME = values.Value(environ_prefix='KUBEPORTAL')
    ADMIN_EMAIL = values.Value(environ_prefix='KUBEPORTAL')
    ADMINS = [(ADMIN_NAME, ADMIN_EMAIL), ]


class Development(Common):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]

    INSTALLED_APPS = Common.INSTALLED_APPS + ['test_pep8', ]
    TEST_PEP8_IGNORE = ['E501', ]
    PROJECT_DIR = os.path.dirname(__file__)
    TEST_PEP8_DIRS = [os.path.dirname(PROJECT_DIR), ]
    TEST_PEP8_EXCLUDE = ['.env', '.venv', 'env', 'venv', ]

    CLUSTER_API_SERVER = values.Value(
        "#missing setting#", environ_prefix='KUBEPORTAL')
    DEBUG = True

    REDIRECT_HOSTS = ['localhost', '127.0.0.1']

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_HOST = values.Value('localhost', environ_prefix='KUBEPORTAL')


class Production(Common):
    CLUSTER_API_SERVER = values.Value('', environ_prefix='KUBEPORTAL')
    DEBUG = False

    DATABASE_URL = values.DatabaseURLValue(
        'sqlite:////data/kubeportal.sqlite3', environ_prefix='KUBEPORTAL')
    DATABASES = DATABASE_URL

    STATIC_ROOT = values.Value('', environ_prefix='KUBEPORTAL')
    STATICFILES_DIRS = values.TupleValue('', environ_prefix='KUBEPORTAL')

    REDIRECT_HOSTS = values.TupleValue(None, environ_prefix='KUBEPORTAL')

    EMAIL_HOST = values.Value('localhost', environ_prefix='KUBEPORTAL')
