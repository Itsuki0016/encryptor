from django.urls import path
from . import views

urlpatterns = [
    path('', views.encrypt_view, name='home'),  # ルートURLを暗号化ページに設定
    path('encrypt/', views.encrypt_view, name='encrypt'),
    path('decrypt/', views.decrypt_view, name='decrypt'),
    path('history/', views.history_view, name='history'),
    path('logout/', views.logout_view, name='logout'),  # カスタムログアウトビューを追加
]
