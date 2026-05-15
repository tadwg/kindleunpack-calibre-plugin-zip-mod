# KindleUnpack - The Plugin + ZIP mod

**[🌐 Web版（ブラウザで変換）](https://tadwg.github.io/kindleunpack-calibre-plugin-zip-mod/)** — AZW3をサーバに送信せずブラウザ内で変換できます。

本forkにおけるcalibre/Python 3.14対応への移植作業は、[Claude Sonnet 4.6](https://www.anthropic.com/claude)（Anthropic）の支援により行われました。

---

## calibre プラグイン版

calibre用KindleUnpackプラグインを改造して、AZW3を画像のみのZIPとしても出力できるようにしたものです。
最新のcalibre（v6以降 / Python 3.13+）に対応しています。

### ダウンロード

**[⬇ 最新版をダウンロード（Releases）](https://github.com/tadwg/kindleunpack-calibre-plugin-zip-mod/releases/latest/download/KindleUnpack-ZIP-mod.zip)**

`master` に push されるたびに GitHub Actions が自動でZIPを生成します。

リポジトリをクローンして手動でビルドすることもできます：

```bash
git clone https://github.com/tadwg/kindleunpack-calibre-plugin-zip-mod.git
cd kindleunpack-calibre-plugin-zip-mod
python3 build.py
```

`KindleUnpack-ZIP-mod.zip` が生成されます。

### インストール方法

1. 上のリンクから `KindleUnpack-ZIP-mod.zip` をダウンロード
2. calibreを開き、「環境設定」→「プラグイン」→「ファイルからプラグインをロード」
3. ZIPファイルを選択してインストール
4. calibreを再起動

### 使用方法

KindleUnpackのメニューに「KF8 to ZIP」の項目が追加されているので、それを実行してください。

DumpAZW6を使用したHD画像の差し替え機能を使うには、プラグインの設定からKindle Contentディレクトリの場所を指定してください。該当書籍のディレクトリ（`*_EBOK`）に`.res`ファイルがあれば自動的に差し替えて出力します。

### 機能

- **ZIP出力**: AZW3を画像のみのZIPとして出力
- **EPUB出力**: AZW3をEPUBに変換
- **DumpAZW6統合**: `.res`ファイルがあればHD画像を差し替えて出力
- **画像連番**: `00001`始まり（DumpAZW6出力と統一）
- **JPEG拡張子**: `.jpeg` → `.jpg` に統一
- **ZIP圧縮タイプ**: デフォルトで無圧縮（STORE）、設定でDEFLATEに変更可能
- **一時ファイル削除**: 変換後に一時ファイルを自動削除（設定で変更可能）

### 動作確認環境

- calibre 9.8 (Python 3.14)

---

## Web版（ブラウザで変換）

**URL**: https://tadwg.github.io/kindleunpack-calibre-plugin-zip-mod/

[Pyodide](https://pyodide.org/)（WebAssembly版のCPython）を使用しています。[kevinhendricks/KindleUnpack](https://github.com/kevinhendricks/KindleUnpack) をベースにした `kindleunpackcore/` をそのままブラウザ内で実行するため、calibreプラグイン版と同じコードで動作します。ファイルはサーバに送信されず、すべての処理がブラウザ内で完結します。

### 使用方法

1. ページを開き「Pyodide をロード」をクリック（初回は30〜60秒かかります）
2. 「kindleunpackcore をロード」をクリック
3. AZW3ファイルをドロップまたは選択
4. 出力形式（EPUB / ZIP）を選んで「変換を実行」
5. 完了後、ダウンロードリンクが表示されます

### 制限事項

- **HD画像差し替え非対応**: DumpAZW6による`.res`ファイルからのHD画像差し替えは、ブラウザ環境では利用できません（`.res`ファイルはKindleアプリのローカルフォルダに存在するため）
- **初回ロードが重い**: Pyodide本体（約30MB）のダウンロードが必要です
- **大容量ファイル**: ブラウザのメモリ制限により、非常に大きなファイルは処理できない場合があります

---

## ディレクトリ構成

```
kindleunpack-calibre-plugin-zip-mod/
├── action.py              # メニュー・変換フロー（dougmassay版ベース + ZIP mod）
├── config.py              # 設定UI（ZIP mod設定を追加）
├── dialogs.py             # 進捗ダイアログ
├── mobi_stuff.py          # calibreとコアの橋渡し（unpackZIP()追加）
├── utilities.py           # ユーティリティ
├── __init__.py            # プラグイン情報
├── kindleunpackcore/      # 変換コア（以下3リポジトリを統合）
│   ├── kindleunpack.py    # メインロジック（KindleUnpack + ZIP mod）
│   ├── unpack_structure.py# ZIP/EPUB出力（ZIP mod追加）
│   ├── mobi_*.py          # MOBIパーサ群
│   ├── DumpAZW6_v01.py    # HD画像抽出（junk2ool版、Python 3対応済み）
│   ├── imghdr.py          # 画像形式判定（Python 3.13以降対応）
│   └── ...
└── docs/                  # GitHub Pages（Web版）
    ├── index.html         # Wasm変換UI
    └── kindleunpackcore/  # Web版用コア（masterと共通）
```

### kindleunpackcore/ の出どころ

| ファイル | 出どころ |
|---|---|
| `kindleunpack.py`、`mobi_*.py`、`unpack_structure.py`、`compatibility_utils.py`、`imghdr.py`、`unipath.py` 等 | [kevinhendricks/KindleUnpack](https://github.com/kevinhendricks/KindleUnpack) commit `4c3e1a44` |
| `DumpAZW6_v01.py` | [junk2ool/kindleunpack-calibre-plugin-zip-mod](https://github.com/junk2ool/kindleunpack-calibre-plugin-zip-mod) v0.3 |
| `kindleunpack.py`・`unpack_structure.py` へのZIP mod追加部分 | 同上 |
| プラグイン本体（`action.py` 等） | [dougmassay/kindleunpack-calibre-plugin](https://github.com/dougmassay/kindleunpack-calibre-plugin) v0.83.8 |

---

## 元のプラグイン (junk2ool版) からの主な変更点

- **最新calibreコア対応**: KindleUnpack v0.83.8ベースのコアを使用
- **Python 3.13/3.14対応**: 標準ライブラリから削除された `imghdr`・`distutils` を代替実装に置き換え
- **qt.core対応**: calibre 6以降のQt APIインポートに対応
- **DumpAZW6**: Python 3構文に完全対応（`print()`、`except X as e:`、`bytes`比較、`open()`等）
- **JPEG拡張子修正**: `get_image_type()` が返す `'jpeg'` を `'jpg'` に統一

---

## ライセンス

GNU General Public License v3.0

## クレジット

本forkにおけるcalibre/Python 3.14対応への移植作業は、[Claude Sonnet 4.6](https://www.anthropic.com/claude)（Anthropic）の支援により行われました。
