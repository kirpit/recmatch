import os

# Django settings for recmatch project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


ABSOLUTE_PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.abspath(os.path.join(ABSOLUTE_PROJECT_PATH, '../media/'))
RESUMES_ROOT = os.path.abspath(os.path.abspath(os.path.join(MEDIA_ROOT, 'resumes/')))

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.abspath(os.path.join(ABSOLUTE_PROJECT_PATH, '../static/'))

# URL that handles the media, static, etc.
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'



#DATABASE_ENGINE = 'sql_server.pyodbc'
#DATABASE_NAME = 'the_database'
#DATABASE_USER = 'django_access'
#DATABASE_PASSWORD = 'guessme'
#DATABASE_OPTIONS = {
#    'driver': 'FreeTDS',
#    'dsn': 'MyDSN', # ODBC DSN name defined in your odbc.ini
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '%s/dev.db' % ABSOLUTE_PROJECT_PATH,                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Australia/Sydney'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# Additional locations of static files
STATICFILES_DIRS = (
#    os.path.abspath(os.path.join(ABSOLUTE_PROJECT_PATH, 'static_extra/')),
)

FIXTURE_DIRS = (
    os.path.abspath(os.path.join(ABSOLUTE_PROJECT_PATH, 'common/fixtures/')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '5ck$c_0j!t8jd06b1cy@6+fh30!kwjp%7!t-^bg4l$w%2q*epw'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',

    # django 1.2 only
#    'django.contrib.messages.context_processors.messages',

    # required by django-admin-tools
    'django.core.context_processors.request',
)

LOCAL_APPS = (
    # local apps
    'common',
    'jobs',
    'staffs',
    'employers',
    'jobseekers',
    'specs',
    'industries',
    'matching',
    'contracts',
    'timesheets',
)

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
#    'dilla',
    'autofixture',
) + LOCAL_APPS


# dilla database dummy spaming
#DICTIONARY = "/usr/share/dict/words"
#DILLA_USE_LOREM_IPSUM = False # set to True ignores dictionary
#DILLA_APPS = LOCAL_APPS
##DILLA_EXCLUDE_MODELS = ()
#DILLA_EXCLUDE_MODELS = ('jobs.models.Job', )
#DILLA_SPAMLIBS = ('', )

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
