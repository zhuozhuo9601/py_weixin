# 请求地址
import requests

url = "http://reg.hongchenzx.com/voice/vcode.php"
# 发送get请求
r = requests.get(url)
f = open('valcode.png', 'wb')
# 将response的二进制内容写入到文件中
f.write(r.content)
# 关闭文件流对象
f.close()
print(r.content)
