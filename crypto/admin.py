# crypto/admin.py
from django.contrib import admin
from .models import CryptoLog

admin.site.register(CryptoLog)
