#!/bin/bash
# プロジェクトの初期化とサーバー起動スクリプト

echo "🔐 Encryptor プロジェクトの初期化を開始します..."

# データベースのマイグレーション
echo "データベースのマイグレーションを実行中..."
python manage.py makemigrations
python manage.py migrate

# 管理者ユーザーの作成（既に存在する場合はスキップ）
echo "管理者ユーザーの作成..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('管理者ユーザー admin が作成されました（パスワード: admin123）')
else:
    print('管理者ユーザーは既に存在します')
"

# テストユーザーの作成
echo "テストユーザーの作成..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='testuser').exists():
    User.objects.create_user('testuser', 'test@example.com', 'testpass123')
    print('テストユーザー testuser が作成されました（パスワード: testpass123）')
else:
    print('テストユーザーは既に存在します')
"

echo "🚀 セットアップが完了しました！"
echo "サーバーを起動しています..."
python manage.py runserver
