"""
暗号化・復号化ユーティリティ関数集

このモジュールは様々な暗号化方式の実装を提供します。
各暗号化方式には対応する復号化関数も含まれています。

対応している暗号化方式:
- Caesar暗号: 文字を固定数だけシフト
- Base64: Base64エンコード/デコード
- ランダム置換暗号: アルファベットをランダムに置換
- モールス信号: モールス信号形式でエンコード
- ROT13: 13文字シフトのCaesar暗号
- Atbash暗号: アルファベットを逆順に置換
- Vigenère暗号: 鍵を使用した多表換字暗号
- 数字置換暗号: 文字を数字に置換
- Binary暗号: テキストを二進数で表現
"""

import base64
import random
import string


def caesar_encrypt(text, shift=3):
    """
    Caesar暗号による暗号化
    
    各文字を指定されたシフト数だけアルファベット順で移動させます。
    
    Args:
        text (str): 暗号化対象のテキスト
        shift (int): シフト数（デフォルト: 3）
    
    Returns:
        str: 暗号化されたテキスト
    """
    result = ''
    for char in text:
        if char.isalpha():
            # 大文字・小文字の判定とベース文字の設定
            base = ord('A') if char.isupper() else ord('a')
            # シフト処理（26文字でのループ処理）
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # アルファベット以外はそのまま
            result += char
    return result


def caesar_decrypt(text, shift=3):
    """
    Caesar暗号による復号化
    
    暗号化時のシフトを逆に適用して元のテキストを復元します。
    
    Args:
        text (str): 復号化対象のテキスト
        shift (int): 暗号化時のシフト数（デフォルト: 3）
    
    Returns:
        str: 復号化されたテキスト
    """
    return caesar_encrypt(text, -shift)


def base64_encrypt(text):
    """
    Base64による暗号化（エンコード）
    
    テキストをBase64形式でエンコードします。
    
    Args:
        text (str): 暗号化対象のテキスト
    
    Returns:
        str: Base64でエンコードされたテキスト
    """
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    return encoded_bytes.decode('utf-8')


def base64_decrypt(encoded):
    """
    Base64による復号化（デコード）
    
    Base64でエンコードされたテキストを元のテキストに復元します。
    
    Args:
        encoded (str): Base64でエンコードされたテキスト
    
    Returns:
        str: 復号化されたテキスト
    """
    decoded_bytes = base64.b64decode(encoded.encode('utf-8'))
    return decoded_bytes.decode('utf-8')


def generate_random_mapping():
    """
    ランダム置換暗号用のマッピング辞書を生成
    
    アルファベット26文字をランダムに並び替えて、
    各文字の置換マッピングを作成します。
    
    Returns:
        dict: 元の文字から置換後の文字へのマッピング辞書
    """
    alphabet = string.ascii_lowercase
    shuffled = list(alphabet)
    random.shuffle(shuffled)  # リストをランダムにシャッフル
    return dict(zip(alphabet, shuffled))


def random_substitution_encrypt(text):
    """
    ランダム置換暗号による暗号化
    
    アルファベットをランダムに置換して暗号化します。
    復号化に必要なマッピング情報も暗号文に含めます。
    
    Args:
        text (str): 暗号化対象のテキスト
    
    Returns:
        str: 暗号化されたテキスト（マッピング情報付き）
    """
    mapping = generate_random_mapping()
    result = ''
    # マッピング情報を文字列として保存（復号時に使用）
    mapping_str = ''.join([f"{k}{v}" for k, v in mapping.items()])
    
    for char in text:
        if char.lower() in mapping:
            if char.isupper():
                # 大文字の場合は置換後も大文字にする
                result += mapping[char.lower()].upper()
            else:
                result += mapping[char.lower()]
        else:
            # アルファベット以外はそのまま
            result += char
    
    # マッピング情報を暗号文の最後に追加（|で区切り）
    return f"{result}|{mapping_str}"


def random_substitution_decrypt(encrypted_text):
    """
    ランダム置換暗号による復号化
    
    暗号文に含まれるマッピング情報を使用して元のテキストを復元します。
    
    Args:
        encrypted_text (str): 暗号化されたテキスト（マッピング情報付き）
    
    Returns:
        str: 復号化されたテキスト、またはエラーメッセージ
    """
    try:
        # 暗号文とマッピング情報を分離
        text_part, mapping_part = encrypted_text.split('|')
        
        # マッピング情報を復元（逆マッピングを作成）
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


# モールス信号のマッピング辞書
# 国際モールス符号に基づく文字とモールス符号の対応表
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}


def morse_encrypt(text):
    """
    モールス信号風暗号化
    
    テキストを国際モールス符号に変換します。
    スペースは「/」で表現され、各文字は空白で区切られます。
    
    Args:
        text (str): 暗号化対象のテキスト
    
    Returns:
        str: モールス信号で表現されたテキスト
    """
    result = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            result.append(MORSE_CODE_DICT[char])
        else:
            # マッピングに対応しない文字はそのまま保持
            result.append(char)
    return ' '.join(result)


def morse_decrypt(morse_text):
    """
    モールス信号風復号化
    
    モールス符号を元のテキストに変換します。
    各モールス符号は空白で区切られている必要があります。
    
    Args:
        morse_text (str): モールス符号で表現されたテキスト
    
    Returns:
        str: 復号化されたテキスト
    """
    # 逆マッピング辞書を作成（モールス符号→文字）
    reverse_morse = {v: k for k, v in MORSE_CODE_DICT.items()}
    
    morse_words = morse_text.split(' ')
    result = []
    
    for morse_char in morse_words:
        if morse_char in reverse_morse:
            result.append(reverse_morse[morse_char])
        elif morse_char == '':
            # 空文字列は無視
            continue
        else:
            # 対応しないモールス符号はそのまま保持
            result.append(morse_char)
    
    return ''.join(result)


def rot13_encrypt(text):
    """
    ROT13暗号による暗号化
    
    Caesar暗号の特殊なケースで、13文字シフトします。
    ROT13は自己逆変換のため、同じ処理で暗号化・復号化が可能です。
    
    Args:
        text (str): 暗号化対象のテキスト
    
    Returns:
        str: ROT13で暗号化されたテキスト
    """
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # 13文字シフト（26文字の半分）
            result += chr((ord(char) - base + 13) % 26 + base)
        else:
            result += char
    return result


def rot13_decrypt(text):
    """
    ROT13暗号による復号化
    
    ROT13は自己逆変換のため、暗号化と同じ処理を適用します。
    
    Args:
        text (str): 復号化対象のテキスト
    
    Returns:
        str: 復号化されたテキスト
    """
    return rot13_encrypt(text)


def atbash_encrypt(text):
    """
    Atbash暗号による暗号化
    
    アルファベットを逆順に置換します（A↔Z, B↔Y, ...）。
    古代ヘブライ語の暗号化技法に基づいています。
    
    Args:
        text (str): 暗号化対象のテキスト
    
    Returns:
        str: Atbash暗号で暗号化されたテキスト
    """
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                # 大文字: A=Z, B=Y, C=X, ...
                result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                # 小文字: a=z, b=y, c=x, ...
                result += chr(ord('z') - (ord(char) - ord('a')))
        else:
            result += char
    return result


def atbash_decrypt(text):
    """
    Atbash暗号による復号化
    
    Atbashは自己逆変換のため、暗号化と同じ処理を適用します。
    
    Args:
        text (str): 復号化対象のテキスト
    
    Returns:
        str: 復号化されたテキスト
    """
    return atbash_encrypt(text)


def vigenere_encrypt(text, keyword="ENCRYPT"):
    """
    Vigenère暗号による暗号化
    
    キーワードを使用した多表換字暗号です。
    各文字をキーワードの対応する文字分だけシフトします。
    
    Args:
        text (str): 暗号化対象のテキスト
        keyword (str): 暗号化に使用するキーワード（デフォルト: "ENCRYPT"）
    
    Returns:
        str: Vigenère暗号で暗号化されたテキスト
    """
    result = ''
    keyword = keyword.upper()
    keyword_index = 0
    
    for char in text:
        if char.isalpha():
            # キーワードの対応する文字からシフト量を計算
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            keyword_index += 1
        else:
            result += char
    return result


def vigenere_decrypt(text, keyword="ENCRYPT"):
    """
    Vigenère暗号による復号化
    
    暗号化時と同じキーワードを使用して、シフトを逆に適用します。
    
    Args:
        text (str): 復号化対象のテキスト
        keyword (str): 暗号化時に使用したキーワード（デフォルト: "ENCRYPT"）
    
    Returns:
        str: 復号化されたテキスト
    """
    result = ''
    keyword = keyword.upper()
    keyword_index = 0
    
    for char in text:
        if char.isalpha():
            # キーワードの対応する文字からシフト量を計算（逆方向）
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
            keyword_index += 1
        else:
            result += char
    return result


def number_encrypt(text):
    """
    数字置換暗号による暗号化
    
    各アルファベットを対応する数字に置換します（A=01, B=02, ...）。
    
    Args:
        text (str): 暗号化対象のテキスト
    
    Returns:
        str: 数字で表現されたテキスト
    """
    result = []
    for char in text:
        if char.isalpha():
            if char.isupper():
                # 大文字: A=01, B=02, ..., Z=26
                result.append(str(ord(char) - ord('A') + 1).zfill(2))
            else:
                # 小文字も同様に処理
                result.append(str(ord(char) - ord('a') + 1).zfill(2))
        else:
            # アルファベット以外はそのまま
            result.append(char)
    return ''.join(result)


def number_decrypt(text):
    """
    数字置換暗号による復号化
    
    2桁の数字を対応するアルファベットに復元します。
    
    Args:
        text (str): 数字で表現されたテキスト
    
    Returns:
        str: 復号化されたテキスト
    """
    result = ''
    i = 0
    while i < len(text):
        if text[i:i+2].isdigit():
            num = int(text[i:i+2])
            if 1 <= num <= 26:
                # 1-26の範囲であればアルファベットに変換
                result += chr(ord('A') + num - 1)
                i += 2
            else:
                # 範囲外の数字はそのまま
                result += text[i]
                i += 1
        else:
            # 数字以外はそのまま
            result += text[i]
            i += 1
    return result


def binary_encrypt(text):
    """
    Binary暗号による暗号化
    
    各文字をASCIIコードの8ビット二進数表現に変換します。
    
    Args:
        text (str): 暗号化対象のテキスト
    
    Returns:
        str: 二進数で表現されたテキスト（空白区切り）
    """
    result = []
    for char in text:
        # 文字のASCIIコードを8桁の二進数に変換
        binary = bin(ord(char))[2:].zfill(8)
        result.append(binary)
    return ' '.join(result)


def binary_decrypt(text):
    """
    Binary暗号による復号化
    
    空白区切りの二進数を元の文字に復元します。
    
    Args:
        text (str): 二進数で表現されたテキスト
    
    Returns:
        str: 復号化されたテキスト、またはエラーメッセージ
    """
    try:
        binary_codes = text.split(' ')
        result = ''
        for binary in binary_codes:
            if binary:
                # 二進数を整数に変換してからASCII文字に変換
                result += chr(int(binary, 2))
        return result
    except:
        return "[エラー] 復号に失敗しました"
