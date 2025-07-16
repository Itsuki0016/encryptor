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

### 自動セットアップ（推奨）
```bash
git clone git@github.com:your-username/encryptor.git
cd encryptor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./setup_and_run.sh
```

### 手動セットアップ
```bash
git clone git@github.com:your-username/encryptor.git
cd encryptor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### デフォルトユーザー
- 管理者: `admin` / `admin123`
- テストユーザー: `testuser` / `testpass123`

---

## 🎯 使用方法

1. ブラウザで `http://127.0.0.1:8000/` にアクセス
2. ログイン画面でユーザー認証
3. 暗号化したいテキストを入力し、方式を選択
4. 「暗号化する」ボタンをクリック
5. 結果を確認し、必要に応じて復号化も可能
6. 履歴ページで過去の暗号化・復号化記録を確認

---

## 📁 プロジェクト構造

```
encryptor/
├── crypto/                    # メインアプリケーション
│   ├── templates/crypto/      # テンプレート
│   ├── models.py             # データモデル
│   ├── views.py              # ビュー処理
│   ├── forms.py              # フォーム定義
│   ├── utils.py              # 暗号化ユーティリティ
│   └── admin.py              # 管理画面設定
├── encryptor_project/        # Django設定
├── templates/                # 共通テンプレート
├── manage.py                 # Django管理スクリプト
├── setup_and_run.sh          # 自動セットアップスクリプト
└── requirements.txt          # 依存パッケージ
```

