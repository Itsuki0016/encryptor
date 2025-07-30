"""
暗号化アプリケーションのデータモデル定義

このモジュールは暗号化・復号化の履歴を記録するためのモデルを定義しています。
"""

from django.db import models
from django.contrib.auth.models import User


class CryptoLog(models.Model):
    """
    暗号化・復号化の履歴を記録するモデル
    
    このモデルは、ユーザーが実行した暗号化・復号化の処理を記録し、
    履歴として管理するために使用されます。
    """
    
    # 利用可能な暗号化方式の定義
    # タプル形式で(データベース値, 表示名)を指定
    ENCRYPTION_METHODS = [
        ('caesar', 'Caesar暗号'),           # シーザー暗号（文字をずらす）
        ('base64', 'Base64'),              # Base64エンコード
        ('random_substitution', 'ランダム置換暗号'),  # ランダムな文字置換
        ('morse', 'モールス信号風'),         # モールス信号形式
        ('rot13', 'ROT13暗号'),            # ROT13エンコード
        ('atbash', 'Atbash暗号'),          # Atbash暗号（アルファベット逆順）
        ('vigenere', 'Vigenère暗号'),      # ヴィジュネル暗号（鍵付き）
        ('number', '数字置換暗号'),         # 数字による文字置換
        ('binary', 'Binary暗号'),          # 二進数表現
    ]

    # 実行したユーザー（外部キー）
    # カスケード削除でユーザー削除時にログも削除
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # 元のテキスト（暗号化前または復号化後のテキスト）
    original_text = models.TextField()
    
    # 暗号化されたテキスト（暗号化後または復号化前のテキスト）
    encrypted_text = models.TextField()
    
    # 使用した暗号化方式（上記のENCRYPTION_METHODSから選択）
    method = models.CharField(max_length=20, choices=ENCRYPTION_METHODS)
    
    # 操作種別フラグ（False: 暗号化, True: 復号化）
    is_decryption = models.BooleanField(default=False)
    
    # レコード作成日時（自動設定）
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        管理画面などでのオブジェクト表示用文字列
        
        Returns:
            str: "ユーザー名 | 暗号化方式 | 操作種別" の形式
        """
        return f'{self.user.username} | {self.get_method_display()} | {"解読" if self.is_decryption else "暗号"}'
