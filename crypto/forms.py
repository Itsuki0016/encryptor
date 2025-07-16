from django import forms

class EncryptForm(forms.Form):
    text = forms.CharField(
        label="暗号化したい文章",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'ここに暗号化したいテキストを入力してください'
        })
    )
    method = forms.ChoiceField(
        label="暗号方式",
        choices=[
            ('caesar', 'Caesar暗号'),
            ('base64', 'Base64'),
            ('random_substitution', 'ランダム置換暗号'),
            ('morse', 'モールス信号風'),
            ('rot13', 'ROT13暗号'),
            ('atbash', 'Atbash暗号'),
            ('vigenere', 'Vigenère暗号'),
            ('number', '数字置換暗号'),
            ('binary', 'Binary暗号'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

class DecryptForm(forms.Form):
    encrypted = forms.CharField(
        label="復号したい暗号文",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'ここに復号したい暗号文を入力してください'
        })
    )
    method = forms.ChoiceField(
        label="暗号方式",
        choices=[
            ('caesar', 'Caesar暗号'),
            ('base64', 'Base64'),
            ('random_substitution', 'ランダム置換暗号'),
            ('morse', 'モールス信号風'),
            ('rot13', 'ROT13暗号'),
            ('atbash', 'Atbash暗号'),
            ('vigenere', 'Vigenère暗号'),
            ('number', '数字置換暗号'),
            ('binary', 'Binary暗号'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
