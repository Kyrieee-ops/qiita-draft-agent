import os
from strands import tool

NOTES_DIR = "./notes"


@tool
def read_book_memo(filename: str = "book_memo.txt") -> str:
    """読書メモファイル（.txt）を読み込んで本文を返します。

    Args:
        filename: 読み込むファイル名（デフォルト: 'book_memo.txt'）
    """
    file_path = os.path.join(NOTES_DIR, filename)
    if not os.path.exists(file_path):
        return f"エラー: ファイル '{filename}' が見つかりませんでした。"

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"\n[Tool Call] '{filename}' を読み込みました。")
    return content


@tool
def save_qiita_draft(title: str, markdown_content: str) -> str:
    """生成されたQiita記事のMarkdown草案をファイルとして保存します。

    Args:
        title: 記事のタイトル（ファイル名やヘッダーに使用）
        markdown_content: Qiita用に整えられたMarkdown本文
    """
    output_path = "./draft.md"
    file_data = f"# {title}\n\n{markdown_content}"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(file_data)

    print(f"\n[Tool Call] '{output_path}' に記事草案を保存しました。")
    return f"成功: '{output_path}' に草案を保存しました。"