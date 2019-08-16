"""
Django settings for config project.
"""

import os

###############
# Build paths #
###############

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #ファイル変更により修正
PROJECT_NAME = os.path.basename(BASE_DIR)


############
# Security #
############

DEBUG = False

ALLOWED_HOSTS = []

#################
# Core settings #
#################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    #django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    #main アプリ
    'main.apps.MainConfig',
]




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates', 'allauth'), #ログインテンプレート等などを置く場所
            os.path.join(BASE_DIR, 'templates'), #テンプレートを置く場所
        ],
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


WSGI_APPLICATION = 'config.wsgi.application'

##################
# Authentication #
##################

AUTH_USER_MODEL = "main.User" #main/model.pyで設定予定のUserモデルを認証に使用するため

#ログイン処理後に遷移するURL
LOGIN_REDIRECT_URL = 'home'

#ログアウト処理後に遷移するURL
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend', #CustomUserにおいてEmail設定を行っているため設定が必要
)

# 認証方法をメールアドレスにする
ACCOUNT_AUTHENTICATION_METHOD = 'email' 

# メールアドレスをアカウント作成時に要求する
ACCOUNT_EMAIL_REQUIRED = True 

#ユーザー登録確認メールは送信しない　:送信する場合は'option'
ACCOUTN_EMAIL_VERIFICATION = 'none'

#USER名を使用しない（以下をコメントアウトしていので、今回のプロジェクトでは、アカウント作成時に要求する：デフォルト）
#ACCOUNT_USERNAME_REQUIRED = False 

#ログアウトボタンにより、ログアウト画面に遷移せず、即座にリダイレクト先へ遷移
ACCOUNT_LOGOUT_ON_GET = True 

#all-authがサイトを判別するために使用
SITE_ID = 1

############
# Database #
############

DATABASES = {}


############
# Messages #
############

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

###########
# Logging #
###########

LOGGING = {}

#######################
# Password validation #
#######################

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


########################
# Internationalization #
########################

LANGUAGE_CODE = 'ja' #日本用に設定

TIME_ZONE = 'Asia/Tokyo' #日本用に設定

USE_I18N = True

USE_L10N = True

USE_TZ = True


################
# Static files #
################

#静的ファイルを置く場所を設定
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = '/var/www/{}/static'.format(PROJECT_NAME)

#メディアファイルを置く場所を設定
MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/{}/media'.format(PROJECT_NAME)


##########
# Stripe #
##########