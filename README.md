# 🔐 Encryptor

![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![Django](https://img.shields.io/badge/django-5.2.4-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)

Encryptor は、Djangoで構築された高機能な暗号化・復号化Webアプリケーションです。  
ログイン機能付きで、**9種類の暗号化方式**を使用して文字列を暗号化・復号化し、その履歴を保存・閲覧できます。

## 📑 目次

- [主な機能](#-主な機能)
- [対応暗号化方式](#-対応暗号化方式)
- [使用技術](#-使用技術)
- [セットアップ手順](#-セットアップ手順ローカル)
- [使用方法](#-使用方法)
- [機能詳細](#-機能詳細)
- [プロジェクト構造](#-プロジェクト構造)
- [テスト・開発](#-テスト開発)
- [デプロイメント](#-デプロイメント)
- [貢献](#-貢献)
- [ライセンス](#-ライセンス)

---

## 🚀 主な機能

- 🔒 **9種類の暗号化方式**による暗号化・復号化
- � **ユーザー認証**とセッション管理
- � **履歴管理**機能（ユーザーごとの暗号化履歴）
- 🖥️ **レスポンシブデザイン**（Bootstrap使用）
- 🛠️ **管理画面**での履歴管理
- � **自動セットアップ**スクリプト

---

## 🎯 対応暗号化方式

| 暗号化方式 | 説明 | 例 |
|:---|:---|:---|
| **Caesar暗号** | 文字を3文字ずつシフト | `Hello` → `Khoor` |
| **Base64** | 標準的なBase64エンコーディング | `Hello` → `SGVsbG8=` |
| **ランダム置換暗号** | 毎回ランダムな変換規則を生成 | `Hello` → `Yfuur\|...` |
| **モールス信号風** | 文字を . と - に置き換え | `Hello` → `.... . .-.. .-.. ---` |
| **ROT13暗号** | 文字を13文字シフト（自己逆変換） | `Hello` → `Uryyb` |
| **Atbash暗号** | アルファベットを逆順に置換 | `Hello` → `Svool` |
| **Vigenère暗号** | キーワード"ENCRYPT"を使用 | `Hello` → `Lrncm` |
| **数字置換暗号** | 文字を数字に変換 | `Hello` → `0805121215` |
| **Binary暗号** | 文字をバイナリコードに変換 | `Hello` → `01001000 01100101...` |

---

## 🛠 使用技術

- **Python 3.13+**
- **Django 5.2.4**
- **SQLite**（デフォルトDB）
- **Bootstrap 5.3**（フロントエンド）
- **HTML/CSS/JavaScript**

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
- テストユーザー: `testuser` / `testpass123`
- 管理者: `admin` / `admin123`（管理画面用）

---

## 🎯 使用方法

1. **アクセス**: ブラウザで `http://127.0.0.1:8000/` にアクセス
2. **ログイン**: テストユーザーでログイン（`testuser` / `testpass123`）
3. **暗号化**: 
   - 暗号化したいテキストを入力
   - 9種類の暗号化方式から選択
   - 「暗号化する」ボタンをクリック
4. **復号化**:
   - 復号ページで暗号文を入力
   - 対応する暗号化方式を選択
   - 「復号する」ボタンをクリック
5. **履歴確認**: 履歴ページで過去の暗号化・復号化記録を確認

---

## 📸 スクリーンショット

### 暗号化ページ
- 直感的なフォーム入力
- 9種類の暗号化方式選択
- 各方式の詳細説明付き

### 復号ページ
- 暗号文の入力
- 対応方式の選択
- エラーハンドリング

### 履歴ページ
- ユーザーごとの暗号化履歴
- 日時・方式・結果の一覧表示
- 検索・フィルタリング機能

---

## 🔧 機能詳細

### 暗号化機能
- **リアルタイム暗号化**: 選択した方式で即座に暗号化
- **エラーハンドリング**: 不正な入力に対する適切なエラー表示
- **履歴保存**: 全ての暗号化操作を自動保存

### 復号機能
- **逆変換処理**: 各暗号化方式に対応した復号処理
- **自己逆変換**: ROT13やAtbashなどの自己逆変換暗号に対応
- **エラー処理**: 復号失敗時の適切なエラー表示

### ユーザー管理
- **認証システム**: Djangoの標準認証システム使用
- **セッション管理**: ログイン状態の維持
- **ユーザー別履歴**: 各ユーザーの暗号化履歴を個別管理

---

## 🗂️ データベース設計

### CryptoLog モデル
```python
class CryptoLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_text = models.TextField()
    encrypted_text = models.TextField()
    method = models.CharField(max_length=20, choices=ENCRYPTION_METHODS)
    is_decryption = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

### 暗号化方式
- 9種類の暗号化方式をサポート
- 各方式の実装は `utils.py` に分離
- 拡張性を考慮した設計

---

## 📁 プロジェクト構造

```
encryptor/
├── crypto/                    # メインアプリケーション
│   ├── templates/crypto/      # アプリ固有のテンプレート
│   │   ├── encrypt.html      # 暗号化ページ
│   │   ├── decrypt.html      # 復号ページ
│   │   ├── history.html      # 履歴ページ
│   │   ├── result.html       # 結果表示ページ
│   │   └── logout_confirm.html # ログアウト確認ページ
│   ├── migrations/           # データベースマイグレーション
│   ├── models.py             # データモデル（CryptoLog）
│   ├── views.py              # ビュー処理
│   ├── forms.py              # フォーム定義
│   ├── utils.py              # 暗号化ユーティリティ関数
│   ├── admin.py              # 管理画面設定
│   ├── apps.py               # アプリケーション設定
│   └── urls.py               # URL設定
├── encryptor_project/        # Django設定
│   ├── settings.py           # プロジェクト設定
│   ├── urls.py               # メインURL設定
│   ├── forms.py              # カスタム認証フォーム
│   └── wsgi.py               # WSGI設定
├── templates/                # 共通テンプレート
│   ├── base.html             # ベーステンプレート
│   └── login.html            # ログインページ
├── manage.py                 # Django管理スクリプト
├── setup_and_run.sh          # 自動セットアップスクリプト
├── check_environment.sh      # 環境確認スクリプト
├── requirements.txt          # 依存パッケージ
├── db.sqlite3                # SQLiteデータベース
└── README.md                 # このファイル
```

---

## 🧪 テスト・開発

### テストの実行
```bash
python manage.py test crypto
```

### 開発環境の確認
```bash
./check_environment.sh
```

### 管理画面アクセス
```bash
# 管理画面URL: http://127.0.0.1:8000/admin/
# ユーザー: admin / admin123
```

---

## 🚀 デプロイメント

### 本番環境での注意事項
1. **SECRET_KEY**を環境変数で管理
2. **DEBUG = False**に設定
3. **ALLOWED_HOSTS**を適切に設定
4. **静的ファイル**の配信設定
5. **データベース**をPostgreSQLなどに変更

### 推奨設定
```python
# settings.py
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
```

---

## 🤝 貢献

バグ報告や機能要求は、GitHubのIssuesで受け付けています。

### 開発への参加
1. このリポジトリをフォーク
2. 機能ブランチを作成
3. 変更をコミット
4. プルリクエストを作成

---

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

---

## 🔍 追加情報

### 暗号化アルゴリズムについて
- **教育目的**での実装のため、実際のセキュリティ用途には適さない場合があります
- **Caesar暗号**や**ROT13**などは脆弱性があるため、重要な情報の暗号化には使用しないでください
- **Base64**は暗号化ではなくエンコーディングです

### 今後の拡張予定
- [ ] AES暗号の実装
- [ ] RSA暗号の実装
- [ ] ファイル暗号化機能
- [ ] API機能の追加
- [ ] 暗号強度の評価機能

