from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import CryptoLog
from .utils import caesar_encrypt, caesar_decrypt, base64_encrypt, base64_decrypt

class CryptoUtilsTest(TestCase):
    def test_caesar_encrypt_decrypt(self):
        """Caesar暗号の暗号化・復号化テスト"""
        original = "Hello World"
        encrypted = caesar_encrypt(original)
        decrypted = caesar_decrypt(encrypted)
        self.assertEqual(original, decrypted)
    
    def test_base64_encrypt_decrypt(self):
        """Base64の暗号化・復号化テスト"""
        original = "Hello World"
        encrypted = base64_encrypt(original)
        decrypted = base64_decrypt(encrypted)
        self.assertEqual(original, decrypted)

class CryptoViewsTest(TestCase):
    def setUp(self):
        """テストユーザーの作成"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client = Client()
    
    def test_encrypt_view_requires_login(self):
        """暗号化ビューがログインを要求するかテスト"""
        response = self.client.get(reverse('encrypt'))
        self.assertRedirects(response, '/login/?next=/encrypt/')
    
    def test_encrypt_view_logged_in(self):
        """ログイン後の暗号化ビューテスト"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('encrypt'))
        self.assertEqual(response.status_code, 200)
    
    def test_encrypt_post(self):
        """暗号化のPOSTテスト"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('encrypt'), {
            'text': 'Hello World',
            'method': 'caesar'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(CryptoLog.objects.filter(user=self.user).exists())

class CryptoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_crypto_log_creation(self):
        """CryptoLogモデルの作成テスト"""
        log = CryptoLog.objects.create(
            user=self.user,
            original_text='Hello',
            encrypted_text='Khoor',
            method='caesar',
            is_decryption=False
        )
        self.assertEqual(str(log), 'testuser | Caesar暗号 | 暗号')
        self.assertFalse(log.is_decryption)
