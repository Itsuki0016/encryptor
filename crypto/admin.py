# crypto/admin.py
from django.contrib import admin
from .models import CryptoLog

@admin.register(CryptoLog)
class CryptoLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'method', 'is_decryption', 'created_at']
    list_filter = ['method', 'is_decryption', 'created_at']
    search_fields = ['user__username', 'original_text', 'encrypted_text']
    readonly_fields = ['created_at']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
