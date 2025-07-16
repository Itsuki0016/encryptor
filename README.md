# 🔐 Encryptor

Encryptor は、Djangoで構築された暗号化・復号化サイトです。  
ログイン機能付きで、入力した言葉をCaesar暗号またはBase64で変換し、その履歴を保存・閲覧できます。

---

## 🚀 機能

- 🔒 Caesar暗号・Base64 による暗号化
- 🕵️‍♂️ 暗号文の解読機能
- 👤 ユーザーごとのログイン／履歴保存
- 📜 自分だけの暗号変換履歴ページ
- 🧠 Djangoの基礎機能（モデル・フォーム・ビュー）を活用

---

## 🛠 使用技術

- Python 3.x
- Django 4.x
- SQLite（デフォルトDB）
- Bootstrap（フロントスタイル）

---

## 📦 セットアップ手順（ローカル）

```bash
git clone git@github.com:your-username/encryptor.git
cd encryptor
python3 -m venv venv
source venv/bin/activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

