"""
暗号化アプリケーションの設定

このモジュールはDjangoアプリケーション「crypto」の設定を定義します。
アプリケーションの基本的な設定（名前、デフォルトフィールドタイプなど）を管理します。
"""

from django.apps import AppConfig


class CryptoConfig(AppConfig):
    """
    暗号化アプリケーションの設定クラス
    
    Djangoアプリケーション「crypto」の設定を定義します。
    この設定はsettings.pyのINSTALLED_APPSで参照されます。
    """
    
    # 主キーフィールドのデフォルトタイプ
    # BigAutoFieldは64ビット整数の自動インクリメントフィールド
    default_auto_field = 'django.db.models.BigAutoField'
    
    # アプリケーション名
    name = 'crypto'
