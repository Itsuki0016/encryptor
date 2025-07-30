"""
暗号化アプリケーションのURL設定

このモジュールは暗号化アプリケーション（cryptoアプリ）の
URLパターンを定義しています。各URLは対応するビュー関数にマッピングされます。
"""

from django.urls import path
from . import views

# URLパターンの定義
# 各パターンは「パス」「ビュー関数」「URL名」で構成されます
urlpatterns = [
    # ホームページ（暗号化ページにリダイレクト）
    path('', views.encrypt_view, name='home'),
    
    # 暗号化ページ
    path('encrypt/', views.encrypt_view, name='encrypt'),
    
    # 復号化ページ
    path('decrypt/', views.decrypt_view, name='decrypt'),
    
    # 履歴表示ページ
    path('history/', views.history_view, name='history'),
    
    # ログアウト処理（カスタムビューを使用）
    path('logout/', views.logout_view, name='logout'),
]
