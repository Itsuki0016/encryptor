from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EncryptForm, DecryptForm
from .models import CryptoLog
from .utils import caesar_encrypt, caesar_decrypt, base64_encrypt, base64_decrypt

# 🔐 暗号化ビュー
@login_required
def encrypt_view(request):
    if request.method == 'POST':
        form = EncryptForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            method = form.cleaned_data['method']

            if method == 'caesar':
                encrypted = caesar_encrypt(text)
            else:
                encrypted = base64_encrypt(text)

            # DB保存
            CryptoLog.objects.create(
                user=request.user,
                original_text=text,
                encrypted_text=encrypted,
                method=method,
                is_decryption=False
            )

            return render(request, 'crypto/result.html', {
                'result': encrypted,
                'mode': 'encrypt'
            })
    else:
        form = EncryptForm()

    return render(request, 'crypto/encrypt.html', {'form': form})

# 🕵️‍♂️ 復号ビュー
@login_required
def decrypt_view(request):
    if request.method == 'POST':
        form = DecryptForm(request.POST)
        if form.is_valid():
            encrypted = form.cleaned_data['encrypted']
            method = form.cleaned_data['method']

            try:
                if method == 'caesar':
                    decrypted = caesar_decrypt(encrypted)
                else:
                    decrypted = base64_decrypt(encrypted)
            except Exception:
                decrypted = "[エラー] 復号に失敗しました"

            # DB保存
            CryptoLog.objects.create(
                user=request.user,
                original_text=decrypted,
                encrypted_text=encrypted,
                method=method,
                is_decryption=True
            )

            return render(request, 'crypto/result.html', {
                'result': decrypted,
                'mode': 'decrypt'
            })
    else:
        form = DecryptForm()

    return render(request, 'crypto/decrypt.html', {'form': form})

# 📜 履歴表示ビュー
@login_required
def history_view(request):
    logs = CryptoLog.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'crypto/history.html', {'logs': logs})
