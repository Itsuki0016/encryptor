"""
暗号化アプリケーションのビュー定義

このモジュールは暗号化・復号化・履歴表示のWebページ処理を担当します。
ユーザー認証が必要な機能はlogin_requiredデコレータで保護されています。
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import EncryptForm, DecryptForm
from .models import CryptoLog
from .utils import (
    caesar_encrypt, caesar_decrypt, 
    base64_encrypt, base64_decrypt,
    random_substitution_encrypt, random_substitution_decrypt,
    morse_encrypt, morse_decrypt,
    rot13_encrypt, rot13_decrypt,
    atbash_encrypt, atbash_decrypt,
    vigenere_encrypt, vigenere_decrypt,
    number_encrypt, number_decrypt,
    binary_encrypt, binary_decrypt
)


def logout_view(request):
    """
    ログアウト処理のビュー
    
    POSTリクエストでのみログアウトを実行し、GETリクエストの場合は
    確認ページを表示します。これはCSRF攻撃を防ぐためです。
    
    Args:
        request: HTTPリクエストオブジェクト
    
    Returns:
        HttpResponse: ログアウト確認ページまたはリダイレクト
    """
    if request.method == 'POST':
        # POSTリクエストの場合のみログアウト実行
        logout(request)
        messages.success(request, 'ログアウトしました。')
        return redirect('login')
    else:
        # GETリクエストの場合は確認ページを表示
        return render(request, 'crypto/logout_confirm.html')


@login_required
def encrypt_view(request):
    """
    暗号化処理のビュー
    
    ユーザーが入力したテキストを選択された方式で暗号化します。
    処理結果はデータベースに記録され、結果ページに表示されます。
    
    Args:
        request: HTTPリクエストオブジェクト
    
    Returns:
        HttpResponse: 暗号化フォームページまたは結果ページ
    """
    if request.method == 'POST':
        form = EncryptForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            method = form.cleaned_data['method']

            try:
                # 選択された暗号化方式に応じて処理を分岐
                if method == 'caesar':
                    encrypted = caesar_encrypt(text)
                elif method == 'base64':
                    encrypted = base64_encrypt(text)
                elif method == 'random_substitution':
                    encrypted = random_substitution_encrypt(text)
                elif method == 'morse':
                    encrypted = morse_encrypt(text)
                elif method == 'rot13':
                    encrypted = rot13_encrypt(text)
                elif method == 'atbash':
                    encrypted = atbash_encrypt(text)
                elif method == 'vigenere':
                    encrypted = vigenere_encrypt(text)
                elif method == 'number':
                    encrypted = number_encrypt(text)
                elif method == 'binary':
                    encrypted = binary_encrypt(text)
                else:
                    raise ValueError("未対応の暗号方式です")

                # 暗号化結果をデータベースに保存
                CryptoLog.objects.create(
                    user=request.user,
                    original_text=text,
                    encrypted_text=encrypted,
                    method=method,
                    is_decryption=False  # 暗号化フラグ
                )

                messages.success(request, '暗号化が完了しました！')
                return render(request, 'crypto/result.html', {
                    'result': encrypted,
                    'mode': 'encrypt'
                })
            except Exception as e:
                # エラーが発生した場合はメッセージを表示
                messages.error(request, f'暗号化に失敗しました: {str(e)}')
    else:
        # GETリクエストの場合は空のフォームを表示
        form = EncryptForm()

    return render(request, 'crypto/encrypt.html', {'form': form})


@login_required
def decrypt_view(request):
    """
    復号化処理のビュー
    
    ユーザーが入力した暗号文を選択された方式で復号化します。
    処理結果はデータベースに記録され、結果ページに表示されます。
    
    Args:
        request: HTTPリクエストオブジェクト
    
    Returns:
        HttpResponse: 復号化フォームページまたは結果ページ
    """
    if request.method == 'POST':
        form = DecryptForm(request.POST)
        if form.is_valid():
            encrypted = form.cleaned_data['encrypted']
            method = form.cleaned_data['method']

            try:
                # 選択された復号化方式に応じて処理を分岐
                if method == 'caesar':
                    decrypted = caesar_decrypt(encrypted)
                elif method == 'base64':
                    decrypted = base64_decrypt(encrypted)
                elif method == 'random_substitution':
                    decrypted = random_substitution_decrypt(encrypted)
                elif method == 'morse':
                    decrypted = morse_decrypt(encrypted)
                elif method == 'rot13':
                    decrypted = rot13_decrypt(encrypted)
                elif method == 'atbash':
                    decrypted = atbash_decrypt(encrypted)
                elif method == 'vigenere':
                    decrypted = vigenere_decrypt(encrypted)
                elif method == 'number':
                    decrypted = number_decrypt(encrypted)
                elif method == 'binary':
                    decrypted = binary_decrypt(encrypted)
                else:
                    raise ValueError("未対応の暗号方式です")

                # 復号化結果をデータベースに保存
                CryptoLog.objects.create(
                    user=request.user,
                    original_text=decrypted,
                    encrypted_text=encrypted,
                    method=method,
                    is_decryption=True  # 復号化フラグ
                )

                messages.success(request, '復号が完了しました！')
                return render(request, 'crypto/result.html', {
                    'result': decrypted,
                    'mode': 'decrypt'
                })
            except Exception as e:
                # エラーが発生した場合はメッセージを表示
                messages.error(request, f'復号に失敗しました: {str(e)}')
    else:
        # GETリクエストの場合は空のフォームを表示
        form = DecryptForm()

    return render(request, 'crypto/decrypt.html', {'form': form})


@login_required
def history_view(request):
    """
    履歴表示のビュー
    
    ログインユーザーの暗号化・復号化履歴を新しい順で表示します。
    
    Args:
        request: HTTPリクエストオブジェクト
    
    Returns:
        HttpResponse: 履歴表示ページ
    """
    # 現在のユーザーのログを作成日時の降順で取得
    logs = CryptoLog.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'crypto/history.html', {'logs': logs})
