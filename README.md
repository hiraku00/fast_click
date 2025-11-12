# Fast Click

シンプルで使いやすいマウスクリック自動化ツールです。指定した間隔でマウスクリックを自動化し、作業効率を向上させます。

## 主な機能
- マウスの自動クリック（左クリック）
- カスタマイズ可能なクリック間隔（秒単位）
- ホットキーによる直感的な操作
- 軽量でリソース使用量が少ない

## インストール方法

1. Python 3.6以上をインストール
2. 必要なパッケージをインストール:
   ```bash
   pip install pyautogui keyboard
   ```
3. リポジトリをクローン:
   ```bash
   git clone https://github.com/hiraku00/fast_click.git
   cd fast_click
   ```

## 使い方

### 基本的な使い方
```bash
python fast_click.py
```

### カスタム間隔で実行（例：0.5秒間隔）
```bash
python fast_click.py --interval 0.5
```

## 実行時の設定

プログラム起動時に以下の入力を求められます：
1. クリック間隔（秒）: クリックする間隔を秒単位で入力（例: 0.5）
2. 開始ボタン: クリック開始/停止のホットキー（デフォルト: F6）
3. 終了ボタン: プログラム終了のホットキー（デフォルト: F7）

## 実行時の表示

プログラムを実行すると、以下の情報が表示されます：
```
Fast Click ツールを開始します...
現在の設定:
- クリック間隔: [設定した間隔]秒
- 開始/停止: F6
- 終了: F7

'F6' でクリックの開始/停止、'F7' で終了
```

クリック中は以下のように表示が更新されます：
```
[実行中] 次回のクリックまで残り: X.XX秒
```

## ホットキー

| キー | 機能 |
|------|------|
| `F6` | クリックの開始/停止 |
| `F7` | プログラムの終了 |

## 注意事項
- 管理者権限が必要な場合があります
- クリック中はマウスを動かさないでください
- 終了時は必ず`F7`キーを使用してください

## ライセンス

MIT License

Copyright (c) 2025 hiraku00

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
