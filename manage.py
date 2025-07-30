#!/usr/bin/env python
"""
Django コマンドライン管理ユーティリティ

このスクリプトはDjangoプロジェクトの管理タスクを実行するためのコマンドラインツールです。
サーバー起動、マイグレーション、ユーザー作成などの操作に使用されます。

使用例:
    python manage.py runserver        # 開発サーバーの起動
    python manage.py makemigrations   # マイグレーションファイルの作成
    python manage.py migrate          # データベースマイグレーションの実行
    python manage.py createsuperuser  # 管理者ユーザーの作成
"""
import os
import sys


def main():
    """
    Django管理タスクを実行するメイン関数
    
    環境変数でDjango設定モジュールを指定し、
    コマンドライン引数に基づいて適切な管理コマンドを実行します。
    """
    # Django設定モジュールの指定（デフォルト: encryptor_project.settings）
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'encryptor_project.settings')
    
    try:
        # Django管理コマンドの実行
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Djangoのインポートに失敗した場合のエラーメッセージ
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # コマンドライン引数を処理して管理コマンドを実行
    execute_from_command_line(sys.argv)


# スクリプトが直接実行された場合にmain関数を呼び出し
if __name__ == '__main__':
    main()
