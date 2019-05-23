import tkinter as tk  # 导入 Tkinter 库
import re

root = tk.Tk()
root.geometry('800x400')
root.title('remove pdf newline')

label1 = tk.Label(root, text='输入文本：', font=('Arial', 12)).place(x=0, y=50)
t1 = tk.Text(root, height=10)
t1.place(x=80, y=0)

label2 = tk.Label(root, text='输出文本：', font=('Arial', 12)).place(x=0, y=190)
t2 = tk.Text(root, height=20)
t2.place(x=80, y=140)


def convert_text():
    text = t1.get(1.0, 'end')
    text = re.sub('\n', ' ',  text)
    t2.delete(1.0, 'end')
    t2.insert(1.0, text)

def clear_text():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')

tk.Button(root, text='转换', font=('Arial', 12), width=10, height=1, command=convert_text).place(x=680, y = 50)
tk.Button(root, text='清空', font=('Arial', 12), width=10, height=1, command=clear_text).place(x=680, y = 100)
root.mainloop()  # 进入消息循环