import socket

sock = socket.create_connection(("127.0.0.1", 8888))
sock.sendall(b"xyu")
sock.close()
