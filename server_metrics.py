import socket

def run_server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()

    conn, addr = sock.accept()

    while True:
        data = conn.recv(1024).decode("utf-8")
        dd = {}
        kk = data.split(" ")
        if kk[0] == "put":
            print("received %r from %r" % (data, addr))
            conn.sendall(b"ok\n\n")
            metrik_data = (int(kk[3]), float(kk[2]))
            dd[kk[1]].append(metrik_data)
            
        elif kk[0] == "get":
            print("received %r from %r" % (data, addr))

        elif kk[0] == "*":
            print("received %r from %r" % (data, addr))

        else:
            print("received %r from %r" % (data, addr))
            conn.sendall(b"error\nwrong command\n\n")

        print(data)

    conn.close()
    sock.close()


run_server("127.0.0.1", 8888)


