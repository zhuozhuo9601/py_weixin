import json
import os
import socket
import threading
from tkinter import *

import sys

import time
from tkinter import ttk
from tkinter.tix import ComboBox

import redis as redis
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
            c = chat_with(res_dict['data'], '1')
        else:
            password2 = Label(self.window, text='用户名密码不正确', bg='red').place(x=190, y=270)


class chat_with(object):
    """
    进入主界面
    """
    def __init__(self, user_list, tcp_a):
        if tcp_a != '2':
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
        self.canvas = canvas
        conn = redis.Redis(host='localhost', port=6379, password='django_redis')
        # 可以使用url方式连接到数据库
        # conn = Redis.from_url('redis://[:django_redis]@localhost:6379/1')
        user_ip = conn.get('lizhuo01')
        print(str(user_ip.decode()))
        client_value = tcp_client(user_ip)
        self.tcp_value = client_value


    def chat_text(self):
        """
        测试用户输入的信息
        :return:
        """
        user_news = self.t_text.get()
        print('测试用户输入的数据:', user_news)
        self.tcp_value.send(user_news.encode('utf-8'))
        print('发送成功')
        username = Label(self.canvas, text='用户1:').place(x=0, y=40)
        user_message = Label(self.canvas, text=user_news).place(x=20, y=60)

    def chat_client(self, value):
        print(value)
        username = Label(self.canvas, text='用户2:').place(x=0, y=80)
        user_message = Label(self.canvas, text=value).place(x=20, y=100)


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
    print(res_dict)
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


def tcp_server():
    # host = socket.gethostname()
    port = 9010
    # server.py 服务端
    # print('能不能获取主机名字', host)
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM==流式协议：指的就是TCP协议
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # socket()参数中：family（基于……通信）=AF_INET（网络通信）, type（协议）=SOCK_STREAM（TCP协议），TCP协议默认不用写，如果想要写协议必须是：type=socket.SOCK_STREAM
    sk.bind((get_host_ip(), port))
    # sk.bind((host, port))
    sk.listen()
    while True:
        conn, addr = sk.accept()
        while True:
            msg = conn.recv(1024)
            if msg.decode('utf-8').upper() == 'Q':
                break
            print(msg.decode('utf-8'))
            cont = input('内容(输入Q断开)：')
            conn.send(cont.encode('utf-8'))
            if cont.upper() == 'Q':
                break
        print('服务端接收到的数据:', conn, addr)
    # conn.close()
    # sk.close()
    # while True:
    #     client_socket, addr = sk.accept()
    #     print("连接地址: {str(addr)}")
    #
    #     # 错误二、当发来的数据很长时tcp不会等接收完成再执行下一条语句，这里没处理这个问题
    #     result = client_socket.recv(1024 * 1024)
    #     # 问题一、decode默认使用utf-8编码，但当发来的数据有utf-8不可解码内容时会报异常，这里没捕获异常
    #     print("{result.decode()}")
    #
    #     # 错误三、发送时tcp不会等发送完再执行下一条语句，这里没处理这个问题
    #     client_socket.send(result)
    #     # 注意四、如果客户端中的接收代码是和上边错误二一样的，那么没发完也会被客户端reset
    #     client_socket.close()

def tcp_client(user_ip):
    sk = socket.socket()
    sk.connect((user_ip, 9010))
    # while True:
    #     print('客户端连接到服务端')
    #     msg = sk.recv(1024)
    #     if msg.decode('utf-8').upper() == 'Q':
    #         break
    #     print(msg.decode('utf-8'))
    #     cont = input('内容(输入Q断开)：')
    #     sk.send(cont.encode('utf-8'))
    #     if cont.upper() == 'Q':
    #         break
    # sk.close()
    return sk

if __name__ == '__main__':
    # tcp_server()
    # tk_t = tk_t()
    t1 = threading.Thread(target=tcp_server)
    t2 = threading.Thread(target=tk_t)
    t1.start()
    t2.start()

