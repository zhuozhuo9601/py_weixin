import socket

# 获取本地主机名
host = socket.gethostname()
port = 9010
print(type(host), host)
# 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口号
server_socket.bind((host, port))
# 设置最大连接数，超过后排队
server_socket.listen(5)

# 这里实现的是接收客户端发来的数据、打印、然后再原样返回给客户端
while True:
    client_socket, addr = server_socket.accept()
    print("连接地址: {str(addr)}")

    # 错误二、当发来的数据很长时tcp不会等接收完成再执行下一条语句，这里没处理这个问题
    result = client_socket.recv(1024 * 1024)
    # 问题一、decode默认使用utf-8编码，但当发来的数据有utf-8不可解码内容时会报异常，这里没捕获异常
    print("{result.decode()}")

    # 错误三、发送时tcp不会等发送完再执行下一条语句，这里没处理这个问题
    client_socket.send(result)
    # 注意四、如果客户端中的接收代码是和上边错误二一样的，那么没发完也会被客户端reset
    client_socket.close()
