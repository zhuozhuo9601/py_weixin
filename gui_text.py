import json
import os
import tkinter as tk  # 使用Tkinter前需要先导入

import sys

import time
from tkinter import ttk

import requests


class tk_t(object):
    def __init__(self):
        window = tk.Tk()
        self.window = window
        window.title('My Window')
        window.geometry('500x350')
        canvas = tk.Canvas(window, bg='black', height=200, width=500)
        dir_path = os.getcwd()
        c_sys = sys.platform
        if 'win' in str(c_sys):
            image_file = tk.PhotoImage(file=r'D:\Ubuntu\weixin\py_weixin\static\s_back.gif')
        else:
            image_file = tk.PhotoImage(file=r'{}/static/s_back.gif'.format(dir_path))
        image = canvas.create_image(250, 0, anchor='n', image=image_file)
        canvas.pack()
        name = tk.Label(window, text='账号:').place(x=100, y=205)
        work = tk.Label(window, text='密码:').place(x=100, y=230)
        v_name = tk.StringVar()
        v_word = tk.StringVar()
        username = tk.Entry(window, show=None, font=('Arial', 14), textvariable=v_name)
        password = tk.Entry(window, show='*', font=('Arial', 14), textvariable=v_word)

        self.v_name = v_name
        self.v_word = v_word
        username.pack()
        password.pack()
        b = tk.Button(window, text="登陆", command=self.user_value).place(x=160, y=300)
        b_out = tk.Button(window, text="退出", command=window.quit).place(x=270, y=300)
        window.mainloop()

    def user_value(self):
        user_name = self.v_name.get()
        user_word = self.v_word.get()
        user_dict = {
            "username": user_name,
            "password": user_word
        }
        res_dict = user_login(user_dict)
        if res_dict['code'] == '200':
            self.window.destroy()
            time.sleep(1)
            chat_with()
        else:
            password2 = tk.Label(self.window, text='用户名密码不正确', bg='red').place(x=190, y=270)


class chat_with(object):
    def __init__(self):
        chat = tk.Tk()
        chat.title('My Window')
        chat.geometry('500x300')
        tk.Label(chat, text='进入主界面了', bg='red', font=('Arial', 16)).pack()
        chat.mainloop()


def user_login(user_dict):
    url = "http://127.0.0.1:8001/gui_password/"
    data = {'username': user_dict['username'],
            'password': user_dict['password']
            }
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '49',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'sessionid=q74c4gm9tng3nglitay95yqmxsux4dhp',
        'Host': '127.0.0.1:8001',
        'Referer': 'http://127.0.0.1:8001/gui_password/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    res = requests.post(url=url, data=data, headers=headers, verify=False)
    res_dict = json.loads(res.content.decode())
    return res_dict

tk_t()
