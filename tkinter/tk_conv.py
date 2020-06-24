import tkinter as tk

#メインウィンドウの生成
root = tk.Tk()

label = tk.Label(root, text="10->16")
label.pack()

# リターンが押されたときの動作
def func(ev):
    label2.config( text = hex(int(e.get())) )

# ボタン生成時何もしない処理を定義
def f():
    pass

# テキストボックスを生成
e = tk.Entry( root )

# テキストボックスほ配置
e.pack()
e.bind('<Return>', func)

button = tk.Button(root, text='変換', command=f)
button.bind('<Button-1>', func)
button.pack()

label2 = tk.Label(root, text="")
label2.pack()

root.mainloop()

"""
import tkinter as tk
root = tk.Tk()
label = tk.Label( root, text = '10進->16進変換')
label.pack()
e = tk.Entry( root )
e.pack()
def func():
val = e.get()
ans.config( text = hex( int(val) ))
button = tk.Button(root, text='変換', command=func)
button.pack()
ans = tk.Label( root, text = "")
ans.pack()
root.mainloop()
"""