# KindleUnpack - The Plugin + ZIP mod

calibre用KindleUnpackプラグインを改造して、AZW3を画像のみのZIPとしても出力できるようにしたものです。
最新のcalibre（v6以降 / Python 3.13+）に対応しています。

## 元のプラグイン (junk2ool版) からの主な変更点

- **最新calibreコア対応**: KindleUnpack v0.83.8ベースのコアを使用
- **Python 3.13/3.14対応**: 標準ライブラリから削除された `imghdr`・`distutils` を代替実装に置き換え
- **qt.core対応**: calibre 6以降のQt APIインポートに対応
- **DumpAZW6**: Python 3構文（`print()`、`except X as e:`）に対応

## 元のプラグイン (junk2ool版) の機能

- **ZIP出力機能**: AZW3を画像のみのZIPとして出力可能
- **DumpAZW6統合**: resファイルがあればHD画像を差し替えて出力
- **画像連番**: 00001始まりに変更（DumpAZW6出力と統一）
- **JPEG拡張子**: `.jpeg` → `.jpg` に統一
- **ZIP圧縮タイプ**: デフォルトで無圧縮（STORE）、設定でDEFLATEに変更可能
- **一時ファイル削除**: 変換後に一時ファイルを自動削除（設定で変更可能）

## 動作確認環境

- calibre 9.8 (Python 3.14)

## 使用方法

KindleUnpackのメニューに「KF8 to ZIP」の項目が追加されているので、それを実行してください。

DumpAZW6を使用したHD画像の差し替え機能を使うには、設定からKindle Contentディレクトリの場所を指定してください。

## ベース

- オリジナルZIP mod: [junk2ool/kindleunpack-calibre-plugin-zip-mod](https://github.com/junk2ool/kindleunpack-calibre-plugin-zip-mod) v0.3
- [KindleUnpack - The Plugin](https://github.com/dougmassay/kindleunpack-calibre-plugin) v0.83.8
- [DumpAZW6_v01.py](https://gist.github.com/fireattack/99b7d9f6b2896cfa33944555d9e2a158)

## ライセンス

GNU General Public License v3.0

## クレジット

本forkにおけるcalibre/Python 3.14対応への移植作業は、[Claude Sonnet 4.6](https://www.anthropic.com/claude)（Anthropic）の支援により行われました。
