"""
暗号化アプリケーションのフォーム定義

このモジュールは暗号化・復号化のためのWebフォームを定義しています。
ユーザーがテキストと暗号化方式を選択するためのインターフェースを提供します。
"""

from django import forms


class EncryptForm(forms.Form):
    """
    暗号化用のフォーム
    
    ユーザーが暗号化したいテキストと暗号化方式を選択するためのフォームです。
    Bootstrap CSSクラスを使用してスタイリングされています。
    """
    
    # 暗号化対象のテキスト入力フィールド
    text = forms.CharField(
        label="暗号化したい文章",
        widget=forms.Textarea(attrs={
            'class': 'form-control',  # Bootstrapのスタイルクラス
            'rows': 4,                # テキストエリアの行数
            'placeholder': 'ここに暗号化したいテキストを入力してください'
        })
    )
    
    # 暗号化方式の選択フィールド
    method = forms.ChoiceField(
        label="暗号方式",
        choices=[
            ('caesar', 'Caesar暗号'),           # シーザー暗号
            ('base64', 'Base64'),              # Base64エンコード
            ('random_substitution', 'ランダム置換暗号'),  # ランダム置換
            ('morse', 'モールス信号風'),         # モールス信号
            ('rot13', 'ROT13暗号'),            # ROT13エンコード
            ('atbash', 'Atbash暗号'),          # Atbash暗号
            ('vigenere', 'Vigenère暗号'),      # ヴィジュネル暗号
            ('number', '数字置換暗号'),         # 数字置換
            ('binary', 'Binary暗号'),          # 二進数表現
        ],
        widget=forms.Select(attrs={'class': 'form-select'})  # Bootstrapのセレクトスタイル
    )


class DecryptForm(forms.Form):
    """
    復号化用のフォーム
    
    ユーザーが復号化したい暗号文と復号化方式を選択するためのフォームです。
    Bootstrap CSSクラスを使用してスタイリングされています。
    """
    
    # 復号化対象の暗号文入力フィールド
    encrypted = forms.CharField(
        label="復号したい暗号文",
        widget=forms.Textarea(attrs={
            'class': 'form-control',  # Bootstrapのスタイルクラス
            'rows': 4,                # テキストエリアの行数
            'placeholder': 'ここに復号したい暗号文を入力してください'
        })
    )
    
    # 復号化方式の選択フィールド（暗号化時と同じ方式を使用）
    method = forms.ChoiceField(
        label="暗号方式",
        choices=[
            ('caesar', 'Caesar暗号'),           # シーザー暗号
            ('base64', 'Base64'),              # Base64エンコード
            ('random_substitution', 'ランダム置換暗号'),  # ランダム置換
            ('morse', 'モールス信号風'),         # モールス信号
            ('rot13', 'ROT13暗号'),            # ROT13エンコード
            ('atbash', 'Atbash暗号'),          # Atbash暗号
            ('vigenere', 'Vigenère暗号'),      # ヴィジュネル暗号
            ('number', '数字置換暗号'),         # 数字置換
            ('binary', 'Binary暗号'),          # 二進数表現
        ],
        widget=forms.Select(attrs={'class': 'form-select'})  # Bootstrapのセレクトスタイル
    )
