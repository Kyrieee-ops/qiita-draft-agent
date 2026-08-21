import os
import streamlit as st
from strands import Agent
from tools import read_book_memo, save_qiita_draft

# 1. ページ初期設定
st.set_page_config(page_title="Qiita記事草案作成エージェント", layout="wide")
st.title("📝 読書メモ ➔ Qiita記事草案作成エージェント")

# 2. 親エージェントの定義
qiita_agent = Agent(
    name="QiitaDraftAgent",
    system_prompt=(
        "あなたは優秀な技術ブロガー・Qiita記事執筆アシスタントです。\n"
        "1. `read_book_memo` ツールで指定されたメモを取得してください。\n"
        "2. メモの内容を整理し、Qiita用のMarkdown草案を作成してください。\n"
        "3. `save_qiita_draft` ツールで `draft.md` に保存してください。"
    ),
    tools=[read_book_memo, save_qiita_draft],
)

# 3. Web画面のUI作成
# --- ファイル名入力欄を追加 ---
custom_filename = st.text_input(
    "保存するメモのファイル名（省略可）:",
    value="book_memo.txt",
    placeholder="例: aws_agent_memo.txt",
).strip()

# 未入力や拡張子漏れに対応
if not custom_filename:
    memo_filename = "book_memo.txt"
elif not custom_filename.endswith(".txt"):
    memo_filename = f"{custom_filename}.txt"
else:
    memo_filename = custom_filename

memo_path = os.path.join("./notes", memo_filename)

st.subheader("インプット方法を選択してください")
input_method = st.radio(
    "入力方法", ["テキストを直接入力", "ファイルをアップロード"], horizontal=True
)

if input_method == "テキストを直接入力":
    memo_text = st.text_area("読書メモを入力:", height=200)
    if memo_text:
        with open(memo_path, "w", encoding="utf-8") as f:
            f.write(memo_text)

else:
    uploaded_file = st.file_uploader(
        "メモファイル (.txt) を選択", type=["txt"]
    )
    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")
        with open(memo_path, "w", encoding="utf-8") as f:
            f.write(content)
        st.success(f"ファイル '{memo_filename}' として読み込みました！")

# 4. 実行ボタン
if st.button("🚀 Qiita草案を生成する", type="primary"):
    if not os.path.exists(memo_path):
        st.error("メモが入力されていないか、ファイルが選択されていません。")
    else:
        with st.spinner("エージェントが草案を作成中..."):
            # 動的なメモファイル名を親エージェント（プロンプト）に渡す
            user_query = f"{memo_filename} の内容からQiita記事の草案を作成して保存してください。"
            final_output = qiita_agent(user_query)

        st.success("作成が完了しました！")

        # 5. 生成結果の表示とダウンロード
        if os.path.exists("./draft.md"):
            with open("./draft.md", "r", encoding="utf-8") as f:
                draft_content = f.read()

            st.subheader("📄 生成されたQiita草案 (プレビュー)")
            st.markdown(draft_content)

            st.download_button(
                label="📥 draft.md をダウンロード",
                data=draft_content,
                file_name="draft.md",
                mime="text/markdown",
            )