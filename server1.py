import socket

def run_server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()

    conn, addr = sock.accept()

    while True:
        data = conn.recv(1024).decode("utf-8")
        kk = data.split(" ")
        if kk == "put":
            print("received %r from %r" % (data, addr))
            conn.sendall(b"ok\n\n")
        elif kk == "get":
            print("received %r from %r" % (data, addr))

        elif kk == "*":
            print("received %r from %r" % (data, addr))

        else:
            print("received %r from %r" % (data, addr))
            conn.sendall(b"ok\n\n")

        if not data:
            break
        print(data.decode('utf-8'))

    conn.close()
    sock.close()



a = run_server("127.0.0.1", 8888)


