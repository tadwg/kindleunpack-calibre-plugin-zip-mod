# Changelog

## v0.84.0 (2026-05)

このバージョンはClaude Sonnet 4.6（Anthropic）の支援により、
junk2ool版 v0.3 をベースに作業しました。

kindleunpackcore/ の構成と各ファイルの出どころについては [README](README.md#kindleunpackcore-の出どころ) を参照してください。

### 作業環境
- VPS: Rocky Linux 9 / Podman
- テスト環境: calibre 9.8 (Python 3.14, Windows 11)
- 動作確認: AZW3→EPUB変換、AZW3→ZIP変換、.resファイルからのHD画像差し替え

### calibre / Python 3 対応
- KindleUnpack コアを v0.83.8（dougmassay版）ベースに更新
- `qt.core` インポート対応（calibre 6以降）
- `imghdr`（Python 3.13で削除）を同梱の代替実装に置き換え
- `distutils`（Python 3.12で削除）を `shutil` で代替

### DumpAZW6_v01.py の Python 3 完全対応
- `file()` → `open()`
- `unicode()` → `bytes.decode()`
- `xrange()` → `range()`
- `bytes.encode('hex')` → `bytes.hex()`
- `str/bytes` 比較の統一（`b'RBINCONT'`、`b"CONT"` 等）
- `except X, e:` → `except X as e:`
- `print` 文 → `print()` 関数

### ZIP mod 機能（junk2ool版から引き継ぎ）
- AZW3を画像のみのZIPとして出力
- 画像連番を `00001` 始まりに統一
- JPEG拡張子を `.jpg` に統一（`get_image_type()` の戻り値を修正）
- ZIP圧縮タイプ選択（STORE / DEFLATE）
- 変換後の一時ファイル自動削除

### Web版（Wasm）追加
- Pyodide（WebAssembly版CPython）によるブラウザ内変換
- `kindleunpackcore/` をそのままブラウザで実行
- GitHub Pages で配信（`docs/` フォルダ）
- ファイルはサーバに送信されない
