#!/bin/bash
# 開発環境の確認とテストスクリプト

echo "🧪 Encryptor プロジェクトの動作確認を実行します..."

# 仮想環境のアクティベーション確認
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "✅ 仮想環境がアクティブです: $VIRTUAL_ENV"
else
    echo "⚠️  仮想環境がアクティブではありません"
fi

# Djangoの設定確認
echo "🔧 Django設定の確認..."
python manage.py check

# テストの実行
echo "🧪 テストの実行..."
python manage.py test crypto

# マイグレーション確認
echo "🗃️  マイグレーション状況の確認..."
python manage.py showmigrations

# 静的ファイル確認
echo "📁 プロジェクト構造の確認..."
ls -la

echo "✅ 動作確認が完了しました！"
echo "🚀 サーバーを起動する場合は: python manage.py runserver"
