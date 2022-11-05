# youtube download用
import re

from yt_dlp import YoutubeDL

# Tkinter
import tkinter
from PIL import ImageTk, Image
from tkinter import END, messagebox

# 正規表現


# ウィインドウの作成
root = tkinter.Tk()
root.title('DLYOU')
root.iconbitmap("youtube.ico")
root.geometry('400x400')
root.resizable(0, 0)

# ダウンロード用の関数用意
url_n = 0
down_load_url = []


# リストに追加する処理
def add_url():
    ### httpsの形式をチェックする処理
    if re.match("https?://[\w\-\.~!#\$%&'\(\)\*\+,/;=?@\[\]]+", f"{input_download_url.get()}"):
        ulr_list = tkinter.Label(output_frame, text=f"{input_download_url.get()}", bg=output_color)
        # リストに追加する
        down_load_url.append(input_download_url.get())
        ulr_list.pack()
        input_download_url.delete(0, END)
        print(down_load_url)
    else:
        messagebox.showinfo("確認", "URL形式で入力してください")

# youtubeダウンロード実行関数
def submit_download():
    # ダウンロード対象の数を指定
    # print(len(down_load_url))
    messagebox.askyesno("確認", f"`ダウンロード数は{len(down_load_url)}です。\n処理を開始しますか？")

    ydl_opts = {'format': 'best'}
    with YoutubeDL(ydl_opts) as ydl:
        for url in down_load_url:
            result = ydl.download([url])

    messagebox.showinfo("終了", f"ダウンロードが完了しました。")



# 色の定義
output_color = "#A9A9A9"

# フレームの作成
input_frame = tkinter.Frame(root, bg="gray")
output_frame = tkinter.LabelFrame(root, bg=output_color)
do_frame = tkinter.Frame(root, bg="#D4ECEA")

input_frame.pack(pady=10)  # これを入力することで画面に対象のフレームが表示
output_frame.pack(fill='both', expand=True, padx=(20, 20), pady=(0, 10))
do_frame.pack(pady=15)

# ボタン画像の読み込み
add_img = ImageTk.PhotoImage(Image.open('add_url.png'))
do_img = ImageTk.PhotoImage(Image.open('download.png'))

# 対象URLの入力作成 & 追加ボタンの生成
input_download_url = tkinter.Entry(input_frame, width=30)
input_download_url.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

add_url_button = tkinter.Button(input_frame, image=add_img, command=add_url)
add_url_button.grid(row=0, column=3, padx=10, pady=10, )

do_button = tkinter.Button(do_frame, text="DLYOU!", command=submit_download)
do_button.grid(row=2, column=2, padx=5, pady=5)


# input_download_url.insert(0, "ダウンロードURL")



# ウィンドウのループ処理
root.mainloop()

"""
メモ
#1 PILインストールに失敗
pillowをインストールしたらうまくいった。

#2 icoのサイズはどうするの
48×48
ここに色々ある
https://icon-icons.com/ja/%E3%82%A2%E3%82%A4%E3%82%B3%E3%83%B3/youtube/13475

#3 いちいち立ち上げたアプリ落とすのXは面倒臭い
command + w

#4 改行

#5 アプリの終了

#5 テスト用URL
https://www.youtube.com/watch?v=6orPp5R79MY&list=RDCMUCFbp2XdRpKfk7mYt_uT8dxw&index=5
https://www.youtube.com/watch?v=2SnZf4b6MHM


https?://[\w\-\.~!#\$%&'\(\)\*\+,/;=?@\[\]]+

"""
