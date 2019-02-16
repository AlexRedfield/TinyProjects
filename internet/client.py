'''
import socket

socket.setdefaulttimeout(5)
s=socket.socket()
s.connect(("192.168.95.145",21))
ans=s.recv(1024)
print(ans)
'''
# 客户端

import socket

BUF_SIZE = 1024  # 设置缓冲区的大小
server_addr = ('127.0.0.1', 8888)  # IP和端口构成表示地址
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 返回新的socket对象
client.connect(server_addr)  # 要连接的服务器地址
while True:
    data = input("Please input some string > ")
    if not data:
        break
    client.sendall(data.encode())  # 发送数据到服务器
    data = client.recv(BUF_SIZE).decode()  # 从服务器端接收数据
    if not data:
        break
    print(data)

client.close()
