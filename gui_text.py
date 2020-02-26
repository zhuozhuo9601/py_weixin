import json
import os
import socket
from tkinter import *

import sys

import time
from tkinter import ttk
from tkinter.tix import ComboBox

import requests


class tk_t(object):
    """
    第一个登陆窗口
    """
    def __init__(self):
        window = Tk()
        self.window = window
        window.title('My Window')
        window.geometry('500x350')
        canvas = Canvas(window, bg='black', height=200, width=500)
        dir_path = os.getcwd()
        c_sys = sys.platform
        if 'win' in str(c_sys):
            image_file = PhotoImage(file=r'D:\Ubuntu\weixin\py_weixin\static\s_back.gif')
        else:
            image_file = PhotoImage(file=r'{}/static/s_back.gif'.format(dir_path))
        image = canvas.create_image(250, 0, anchor='n', image=image_file)
        canvas.pack()
        name = Label(window, text='账号:').place(x=100, y=205)
        work = Label(window, text='密码:').place(x=100, y=230)
        v_name = StringVar()
        v_word = StringVar()
        username = Entry(window, show=None, font=('Arial', 14), textvariable=v_name)
        password = Entry(window, show='*', font=('Arial', 14), textvariable=v_word)

        self.v_name = v_name
        self.v_word = v_word
        username.pack()
        password.pack()

        b = Button(window, text="登陆", command=self.user_value).place(x=160, y=300)
        b_out = Button(window, text="退出", command=window.quit).place(x=270, y=300)
        window.mainloop()

    def user_value(self):
        """
        验证账号密码是否正确
        :return:
        """
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
            chat_with(res_dict['data'])
        else:
            password2 = Label(self.window, text='用户名密码不正确', bg='red').place(x=190, y=270)


class chat_with(object):
    """
    进入主界面
    """
    def __init__(self, user_list):
        chat = Tk()
        chat.title('My Window')
        chat.geometry('500x300')
        Label(chat, text='进入主界面了', bg='red', font=('Arial', 16)).pack()
        frame = Frame(chat)
        frame.pack()
        # frame_l = tk.Frame(frame)
        # frame_r = tk.Frame(frame)
        # frame_l.pack(side='left')
        # frame_r.pack(side='right')
        # l1 = tk.Label(frame, text='第一句').pack()
        self.frame = frame
        self.chat = chat
        num_x = 50
        for tk_user in user_list:
            Button(chat, text="{}".format(tk_user), command=self.chat_frame, bg='red').place(x=430, y=num_x)
            num_x += 40
        text_name = StringVar()
        t_text = Entry(chat, show=None, font=('Arial', 14), textvariable=text_name)
        t_text.place(x=0, y=200)

        self.t_text = t_text
        Button(chat, text="发送消息", command=self.chat_text, bg='blue').place(x=430, y=250)
        chat.mainloop()

    def chat_frame(self):
        """
        点击链接其他用户
        :return:
        """
        canvas = Canvas(self.chat, bg='green', height=100, width=300).place(x=0, y=40)

    def chat_text(self):
        """
        测试用户输入的信息
        :return:
        """
        aaa = self.t_text.get()




def user_login(user_dict):
    """
    发送post请求　验证账号密码
    :param user_dict:
    :return:
    """
    url = "http://127.0.0.1:8001/gui_password/"
    ip = get_host_ip()
    data = {'username': user_dict['username'],
            'password': user_dict['password'],
            'ip': ip
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

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

tk_t()
