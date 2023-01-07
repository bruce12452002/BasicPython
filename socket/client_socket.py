import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8888))

data = client_socket.recv(1024)  # 接收 1024 Byte 以內的資料
print(data)
client_socket.close()
