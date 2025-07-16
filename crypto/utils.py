import base64

# Caesar暗号（基本シフト：+3）
def caesar_encrypt(text, shift=3):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Caesar復号（シフトを逆に）
def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

# Base64暗号化
def base64_encrypt(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

# Base64復号
def base64_decrypt(encoded):
    decoded_bytes = base64.b64decode(encoded.encode('utf-8'))
    return decoded_bytes.decode('utf-8')
