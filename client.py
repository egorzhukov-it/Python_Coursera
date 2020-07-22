import socket
import time


class ClientError(Exception):
    def __init__(self):
        print("ClientError")


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def put(self, data_name, data, timestamp=None):

        if timestamp is None:
            timestamp = str(int(time.time()))
        else:
            timestamp = str(timestamp)

        try:
            with socket.create_connection((self.host, self.port)) as sock:
                sock.settimeout(self.timeout)

                sock.sendall(b"put " + data_name.encode('utf-8') + b" " + str(data).encode('utf-8') +
                             b" " + timestamp.encode('utf-8') + b"\n")

                while True:
                    tmp = sock.recv(1024).decode('utf-8').split("\n")
                    print(tmp)
                    if not tmp:
                        break
                    if tmp[0] == "ok":
                        break
                    if tmp[0] == "error":
                        raise ClientError
        except socket.error as err:
            print("ERROR", err)

    def get(self, data_names):
        try:
            with socket.create_connection((self.host, self.port)) as sock:
                sock.settimeout(self.timeout)
                sock.sendall(b"get " + data_names.encode('utf-8') + b"\n")

                while True:
                    tmp = sock.recv(1024).decode('utf-8').split('\n')
                    dd = {}
                    for t in tmp:

                        if t == "ok":
                            continue
                        if t == "":
                            break
                        k = t.split(" ")

                        metrik_data = (int(k[2]), float(k[1]))

                        if str(k[0]) in dd.keys():
                            dd[str(k[0])].append(metrik_data)
                        else:
                            dd[str(k[0])] = [tuple([int(k[2]), float(k[1])])]

                    return dd

        except socket.error as err:
            print(err)

client = Client("127.0.0.1", 8888, 15)

client.put("load", 4, timestamp=5)
client.put("test", 0.5, timestamp=1)
client.put("test", 2.0, timestamp=2)
client.put("test", 0.5, timestamp=3)
client.put("load", 3, timestamp=4)
client.put("load", 4, timestamp=5)
client.get("load")
client.get("*")
