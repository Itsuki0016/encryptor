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
    
    # メインページ（ログイン後のランディングページ）
    path('main/', views.encrypt_view, name='main'),
    
    # 暗号化ページ
    path('encrypt/', views.encrypt_view, name='encrypt'),
    
    # 復号化ページ
    path('decrypt/', views.decrypt_view, name='decrypt'),
    
    # 履歴表示ページ
    path('history/', views.history_view, name='history'),
    
    # 履歴削除機能
    path('history/delete/<int:log_id>/', views.delete_history, name='delete_history'),
    path('history/clear/', views.clear_all_history, name='clear_all_history'),
    
    # ログアウト処理（カスタムビューを使用）
    path('logout/', views.logout_view, name='logout'),
    
    # Ajax API（リアルタイムプレビュー用）
    path('api/encrypt-preview/', views.encrypt_preview, name='encrypt_preview'),
    
    # バッチ処理（複数テキスト処理）
    path('batch/encrypt/', views.batch_encrypt_view, name='batch_encrypt'),
    path('batch/decrypt/', views.batch_decrypt_view, name='batch_decrypt'),
]
