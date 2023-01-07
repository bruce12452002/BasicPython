import socket

"""
    socket.AF_INET	於伺服器與伺服器之間進行串接
    socket.AF_INET6	使用IPv6於伺服器與伺服器之間進行串接
    
    socket.SOCK_STREAM	使用TCP
    socket.SOCK_DGRAM	使用UDP
"""

server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8888))
server_socket.listen(3)  # 最大連接數

while True:
    print("監聽中…")
    client_socket, address = server_socket.accept()
    print(f"{str(address)}")
    client_socket.send("Hello, socket".encode("UTF-8"))
    # client_socket.close()
