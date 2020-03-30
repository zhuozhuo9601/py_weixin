import requests


def lord(code):
    for i in range(0, 200):
        if i < 10:
            i = '0' + str(i)
        url = 'http://reg.hongchenzx.com/reg.php'

        data = {
            'select': "3",
            'username': "zhiaiwoq{}".format(i),
            'passwd': "741741",
            'repeatpasswd': "741741",
            'email': "nono@qq.com",
            'question': "-----",
            'answer': "741741",
            'qq': "847951227",
            'yzm': str(code),
            'Submit': "立即注册"
        }
        headers = {
            'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, image/apng, */*;q=0.8, application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age = 0',
            'Connection': 'keep-alive',
            'Content-Length': 177,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '__cfduid=dcda3066f3ce689a49481db36c6036b3f1585549209; PHPSESSID=ikp34i5aivdat4o81suufmmpo3',
            'Host': 'reg.hongchenzx.com',
            'Origin': 'http://reg.hongchenzx.com',
            'Referer': 'http://reg.hongchenzx.com/',
            'Upgrade - Insecure - Requests': 1,
            'User - Agent': 'Mozilla/5.0(Windows NT 6.1;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }

        req = requests.post(url, data=data, headers=headers)  # 发送post请求，第一个参数是URL，第二个参数是请求数据

        print(req.text)

if __name__ == '__main__':
    # 使用threading模块，threading.Thread()创建线程，其中target参数值为需要调用的方法，同样将其他多个线程放在一个列表中，遍历这个列表就能同时执行里面的函数了
    # threads = [threading.Thread(target=index_method),
    #            threading.Thread(target=code_method)]
    # for t in threads:
    #     # 启动线程
    #     t.start()
    # index_method()
    lord('8317')