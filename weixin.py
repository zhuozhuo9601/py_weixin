import os
import tkinter as tk  # 使用Tkinter前需要先导入

import sys


class tk_t(object):
    def __init__(self):
        # 第1步，实例化object，建立窗口window
        window = tk.Tk()
        # 第2步，给窗口的可视化起名字
        window.title('My Window')
        # 第3步，设定窗口的大小(长 * 宽)
        window.geometry('500x300')  # 这里的乘是小x
        # 第4步，在图形界面上创建 500 * 200 大小的画布并放置各种元素
        canvas = tk.Canvas(window, bg='black', height=200, width=500)
        dir_path = os.getcwd()
        c_sys = sys.platform
        if 'win' in str(c_sys):
            image_file = tk.PhotoImage(file=r'D:\Ubuntu\weixin\py_weixin\static\s_back.gif')
        else:
            image_file = tk.PhotoImage(file='{}/static/s_back.gif'.format(dir_path))
        image = canvas.create_image(250, 0, anchor='n', image=image_file)
        canvas.pack()
        name = tk.Label(window, text='账号:').place(x=100, y=205)
        work = tk.Label(window, text='密码:').place(x=100, y=230)
        v_name = tk.StringVar()
        v_word = tk.StringVar()
        username = tk.Entry(window, show=None, font=('Arial', 14), textvariable=v_name)
        password = tk.Entry(window, show='*', font=('Arial', 14), textvariable=v_word)

        self.v_name=v_name
        self.v_word=v_word
        username.pack()
        password.pack()
        b = tk.Button(window, text="登陆", command=self.user_value).place(x=170, y=260)
        b_out = tk.Button(window, text="退出", command=quit).place(x=280, y=260)
        window.mainloop()
    def user_value(self):
        user_name = self.v_name.get()
        user_word = self.v_word.get()
        user_dict = {
            "username":user_name,
            "pasword":user_word
        }
        print('发送登陆的请求:{}'.format(user_dict))
        return user_dict


    def test_cmd(self, content):
        print(content)

t = tk_t()
