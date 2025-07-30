"""
Django プロジェクトの設定ファイル

暗号化アプリケーション（Encryptor）のDjangoプロジェクト設定。
データベース、認証、テンプレート、静的ファイルなどの設定を定義します。

注意：本番環境では以下の設定を変更してください：
- SECRET_KEY を環境変数で管理
- DEBUG = False に設定
- ALLOWED_HOSTS に適切なホストを追加
- データベース設定を本番用に変更
"""

import os
from pathlib import Path

# プロジェクトのベースディレクトリ
# このファイルの2階層上のディレクトリを指す
BASE_DIR = Path(__file__).resolve().parent.parent

# セキュリティ設定
# 警告：本番環境では環境変数で管理すること
SECRET_KEY = 'django-insecure-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# デバッグモード（本番環境では False に設定）
DEBUG = True

# 許可されたホスト（本番環境では適切なドメインを指定）
ALLOWED_HOSTS = []

# インストール済みアプリケーション
INSTALLED_APPS = [
    # Django標準アプリケーション
    'django.contrib.admin',        # 管理画面
    'django.contrib.auth',         # 認証システム
    'django.contrib.contenttypes', # コンテンツタイプフレームワーク
    'django.contrib.sessions',     # セッション管理
    'django.contrib.messages',     # メッセージフレームワーク
    'django.contrib.staticfiles',  # 静的ファイル管理

    # カスタムアプリケーション
    'crypto',  # 暗号化アプリケーション
]

# ミドルウェア設定（リクエスト・レスポンス処理の順序）
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',      # セキュリティ設定
    'django.contrib.sessions.middleware.SessionMiddleware',  # セッション管理
    'django.middleware.common.CommonMiddleware',          # 共通設定
    'django.middleware.csrf.CsrfViewMiddleware',          # CSRF保護
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 認証
    'django.contrib.messages.middleware.MessageMiddleware',     # メッセージ
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   # クリックジャッキング保護
]

# ルートURL設定ファイルの指定
ROOT_URLCONF = 'encryptor_project.urls'

# テンプレート設定
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 共通テンプレートディレクトリ
        'APP_DIRS': True,  # アプリケーション内のtemplatesディレクトリを検索
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',    # デバッグ情報
                'django.template.context_processors.request',  # リクエスト情報
                'django.contrib.auth.context_processors.auth', # 認証情報
            ],
        },
    },
]

# WSGI アプリケーションの指定
WSGI_APPLICATION = 'encryptor_project.wsgi.application'

# データベース設定
# 開発環境ではSQLiteを使用（本番環境ではPostgreSQLやMySQLを推奨）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# パスワード強度検証設定
# ユーザーパスワードの安全性を確保するためのバリデーター
AUTH_PASSWORD_VALIDATORS = [
    {
        # ユーザー属性（ユーザー名など）との類似性をチェック
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        # 最小文字数をチェック（デフォルト: 8文字）
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        # よく使われるパスワードでないかチェック
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        # 数字のみのパスワードでないかチェック
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 国際化・地域化設定
LANGUAGE_CODE = 'ja'  # 日本語設定

TIME_ZONE = 'Asia/Tokyo'  # 日本時間

USE_I18N = True   # 国際化機能を有効化
USE_TZ = True     # タイムゾーン機能を有効化

# 静的ファイル設定
STATIC_URL = '/static/'  # 静的ファイルのURL

# 認証関連のリダイレクト設定
LOGIN_URL = '/login/'           # ログインページURL
LOGIN_REDIRECT_URL = '/'        # ログイン成功後のリダイレクト先
LOGOUT_REDIRECT_URL = '/login/' # ログアウト後のリダイレクト先

# モデルの主キーフィールドのデフォルト設定
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ログインフォームのカスタムスタイル設定
LOGIN_FORM_WIDGET_ATTRS = {
    'class': 'form-control',
    'placeholder': 'ユーザー名またはパスワードを入力してください'
}
