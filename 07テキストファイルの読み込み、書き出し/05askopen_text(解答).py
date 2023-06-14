
# 練習プログラム7 ファイルをダイアログで選ぶ

"""
- tkinkerモジュールを使用して、GUIで選択したファイルを出力しましょう。
"""

import tkinter as tk
import tkinter.filedialog as fd

# tkアプリウインドウを表示しない
root = tk.Tk()
root.withdraw()

# オープンダイアログを表示する
file_path = fd.askopenfilename(
   title = "ファイルを選んでください。",
   filetypes=[("TEXT", ".txt"), ("TEXT", ".py"), ("HTML", ".html")]
)

# ファイルが選択されたらファイルパス名を出力する
if file_path:
    with open(file_path, "r", encoding="utf_8") as fileobj:    # ファイルを開く
        text = fileobj.read()    # ファイルを読み込む
        print(text)
