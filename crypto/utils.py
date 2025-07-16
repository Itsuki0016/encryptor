import base64
import random
import string

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

# ランダム置換暗号用のマッピング生成
def generate_random_mapping():
    alphabet = string.ascii_lowercase
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))

# ランダム置換暗号（暗号化）
def random_substitution_encrypt(text):
    mapping = generate_random_mapping()
    result = ''
    # マッピングを結果に含めるため、特殊な形式で保存
    mapping_str = ''.join([f"{k}{v}" for k, v in mapping.items()])
    
    for char in text:
        if char.lower() in mapping:
            if char.isupper():
                result += mapping[char.lower()].upper()
            else:
                result += mapping[char.lower()]
        else:
            result += char
    
    # マッピング情報を暗号文の最後に追加（|で区切り）
    return f"{result}|{mapping_str}"

# ランダム置換暗号（復号）
def random_substitution_decrypt(encrypted_text):
    try:
        # 暗号文とマッピング情報を分離
        text_part, mapping_part = encrypted_text.split('|')
        
        # マッピング情報を復元
        mapping = {}
        for i in range(0, len(mapping_part), 2):
            original = mapping_part[i]
            substituted = mapping_part[i+1]
            mapping[substituted] = original
        
        result = ''
        for char in text_part:
            if char.lower() in mapping:
                if char.isupper():
                    result += mapping[char.lower()].upper()
                else:
                    result += mapping[char.lower()]
            else:
                result += char
        
        return result
    except:
        return "[エラー] 復号に失敗しました"

# モールス信号のマッピング
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}

# モールス信号風暗号化
def morse_encrypt(text):
    result = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            result.append(MORSE_CODE_DICT[char])
        else:
            result.append(char)  # 対応しない文字はそのまま
    return ' '.join(result)

# モールス信号風復号
def morse_decrypt(morse_text):
    # 逆マッピングを作成
    reverse_morse = {v: k for k, v in MORSE_CODE_DICT.items()}
    
    morse_words = morse_text.split(' ')
    result = []
    
    for morse_char in morse_words:
        if morse_char in reverse_morse:
            result.append(reverse_morse[morse_char])
        elif morse_char == '':
            continue
        else:
            result.append(morse_char)  # 対応しない文字はそのまま
    
    return ''.join(result)
