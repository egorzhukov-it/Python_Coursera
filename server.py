import asyncio


class DataMetrics:
    dd = {}

    def dd_null(self):
        self.dd = {}

    def put(self, metric_name, metric_value, metric_time):

        metrik_data = (metric_time, metric_value)

        if metric_name in self.dd.keys():
            if metrik_data in self.dd[metric_name]:
                pass
            else:
                self.dd[metric_name].append(metrik_data)
        else:
            self.dd[metric_name] = [tuple([metric_time, metric_value])]

    def get(self, metric_name):

        if metric_name in self.dd.keys():
            ss = {metric_name: self.dd[metric_name]}
            return ss

        elif metric_name == "*":
            return self.dd

        else:
            return None


def run_server(host, port):
    loop = asyncio.get_event_loop()
    echo = asyncio.start_server(handle_echo, host, port)
    server = loop.run_until_complete(echo)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


async def handle_echo(reader, writer):
    while True:
        data = await reader.read(1024)
        # print(data)
        if not data:
            break
        message = data.decode()
        kk = message.split(" ")

        if kk[0] == "put":
            metric_name = str(kk[1])
            metric_value = float(kk[2])
            metric_time = int(kk[3])
            metrics_class.put(metric_name, metric_value, metric_time)

            # addr = writer.get_extra_info("peername")
            # print("received %r from %r" % (message, addr))

            server_data = b"ok\n\n"

            writer.write(server_data)

        elif kk[0] == "get":

            metric_name = str(kk[1]).split("\n")[0]

            get_results = metrics_class.get(metric_name)

            # addr = writer.get_extra_info("peername")
            # print("received %r from %r" % (message, addr))
            metric_list = ""
            if get_results:
                for gg in get_results.keys():
                    ggg = get_results[gg]
                    for aa in ggg:
                        metric_list = metric_list + gg + " " + str(aa[1]) + " " + str(aa[0]) + "\n"
                server_data = b'ok\n' + metric_list.encode('utf-8') + b'\n'
                writer.write(server_data)
            else:
                server_data = b'ok\n\n'
                writer.write(server_data)
        else:
            # addr = writer.get_extra_info("peername")
            # print("received %r from %r" % (message, addr))

            server_data = b'error\nwrong command\n\n'

            writer.write(server_data)

    metrics_class.dd_null()
    writer.close()


metrics_class = DataMetrics()
#a = run_server("127.0.0.1", 8888)
