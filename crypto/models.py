from django.db import models
from django.contrib.auth.models import User

class CryptoLog(models.Model):
    ENCRYPTION_METHODS = [
        ('caesar', 'Caesar暗号'),
        ('base64', 'Base64'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_text = models.TextField()
    encrypted_text = models.TextField()
    method = models.CharField(max_length=20, choices=ENCRYPTION_METHODS)
    is_decryption = models.BooleanField(default=False)  # False: 暗号化, True: 解読
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} | {self.get_method_display()} | {"解読" if self.is_decryption else "暗号"}'
