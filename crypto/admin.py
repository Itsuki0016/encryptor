"""
Django管理画面の設定

このモジュールはDjangoの管理画面でCryptoLogモデルを管理するための
設定を定義しています。管理者はWebブラウザから暗号化履歴を確認・管理できます。
"""

from django.contrib import admin
from .models import CryptoLog


@admin.register(CryptoLog)
class CryptoLogAdmin(admin.ModelAdmin):
    """
    CryptoLogモデルの管理画面設定
    
    暗号化・復号化ログの管理画面での表示・検索・フィルタリング設定を定義します。
    パフォーマンス向上のため、ユーザー情報はselect_relatedで事前取得します。
    """
    
    # 一覧画面で表示するフィールド
    list_display = ['user', 'method', 'is_decryption', 'created_at']
    
    # フィルタリング用のサイドバー項目
    list_filter = ['method', 'is_decryption', 'created_at']
    
    # 検索可能なフィールド（ユーザー名、元テキスト、暗号化テキスト）
    search_fields = ['user__username', 'original_text', 'encrypted_text']
    
    # 編集不可フィールド（作成日時は自動設定のため）
    readonly_fields = ['created_at']
    
    def get_queryset(self, request):
        """
        クエリセットの最適化
        
        ユーザー情報を事前に取得してN+1問題を回避します。
        
        Args:
            request: HTTPリクエストオブジェクト
        
        Returns:
            QuerySet: 最適化されたクエリセット
        """
        return super().get_queryset(request).select_related('user')
