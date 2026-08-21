# 📝 Qiita Draft Agent (読書メモ ➔ Qiita記事草案作成エージェント)

読書メモや技術学習のテキストから、AI エージェントが自動で構造化・整理を行い、Qiita 投稿用の Markdown 記事草案を作成する Web アプリケーションです。

Agents as Tools パターンを採用し、親エージェント（オーケストレーター）が子のツール関数（ファイル読み込み・保存）を動的に呼び出して処理を実行します。

---

## 🚀 特徴

* **柔軟なインプット対応**: Web 画面からの直接テキスト入力、または `.txt` ファイルのアップロードに対応
* **ファイル名の動的設定**: 任意のファイル名を指定してメモを管理可能（未指定時は自動でデフォルト補完）
* **AI エージェントによる自動構造化**: 乱雑な箇条書きメモから「背景・要点・コード・まとめ」などの見やすい Qiita 用 Markdown を自動生成
* **ワンクリックダウンロード**: 生成された `draft.md` をプレビュー表示し、そのままローカルへダウンロード可能

---

## 🛠 技術スタック

* **Language**: Python 3.14
* **Package Manager**: [uv](https://github.com/astral-sh/uv)
* **Agent Framework**: `strands-agents`
* **Web UI**: Streamlit

---

## 📂 プロジェクト構造

```text
qiita-draft-agent/
├── agent-app
│      ├── notes/              # アップロード・入力されたメモの保存先
│      ├── tools.py            # 子ツール（ファイル読み込み・草案保存処理）
│      └── main.py             # Streamlit UI & 親エージェント定義
├── pyproject.toml      # 依存関係管理ファイル
├── README.md
└── draft.md            # 生成されたQiita草案（実行時生成）

```

---

## 💻 起動方法

### 1. リポジトリのクローン & 移動

```bash
git clone <repository-url>
cd qiita-draft-agent

```

### 2. 依存関係のセットアップ

`uv` を使用して仮想環境の作成とパッケージのインストールを行います。

```bash
# 1. Python 3.14 でプロジェクトを初期化
uv init --python 3.14

# 2. strands-agents パッケージを追加
uv add streamlit strands-agents==1.38.0 "boto3[crt]"==1.42.96

```

### 3. アプリケーションの実行

Streamlit サーバーを起動します。

```bash
uv run streamlit run main.py

```

起動後、ターミナルに表示される URL（または Codespaces のポップアップ）から Web 画面にアクセスしてください。

---

## 📖 使い方

1. **ファイル名の指定**: 保存するメモのファイル名を入力します（任意）。
2. **メモの入力**: 「テキストを直接入力」または「ファイルをアップロード」を選択し、読書メモをセットします。
3. **草案の生成**: 「🚀 Qiita草案を生成する」ボタンをクリックします。
4. **確認・保存**: 画面下にプレビュー表示された草案を確認し、「📥 draft.md をダウンロード」ボタンから保存します。