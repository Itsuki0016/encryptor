"""
プロジェクト共通のフォーム定義

このモジュールはプロジェクト全体で使用される共通フォームを定義します。
現在はカスタム認証フォームのみを含んでいます。
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    """
    カスタム認証フォーム
    
    Djangoのデフォルト認証フォームをBootstrapスタイルでカスタマイズしています。
    ユーザー名とパスワードフィールドに適切なプレースホルダーとCSSクラスを追加。
    """
    
    # ユーザー名フィールド（Bootstrap用のスタイル適用）
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',                    # Bootstrapのスタイルクラス
            'placeholder': 'ユーザー名を入力してください'    # プレースホルダーテキスト
        })
    )
    
    # パスワードフィールド（Bootstrap用のスタイル適用）
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',                    # Bootstrapのスタイルクラス
            'placeholder': 'パスワードを入力してください'    # プレースホルダーテキスト
        })
    )
