"""
暗号化プロジェクトのメインURL設定

このファイルはDjangoプロジェクト全体のURL設定を定義します。
管理画面、認証、暗号化アプリケーションのURLパターンを統合します。
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .forms import CustomAuthenticationForm

# プロジェクト全体のURLパターン
urlpatterns = [
    # Django管理画面
    path('admin/', admin.site.urls),
    
    # 暗号化アプリケーションのURL（ルートに配置）
    path('', include('crypto.urls')),
    
    # ログインページ（カスタムフォームを使用）
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',           # カスタムテンプレート
        authentication_form=CustomAuthenticationForm  # カスタム認証フォーム
    ), name='login'),
]
