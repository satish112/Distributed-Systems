import socket
import math
import threading
import time

class process2:

    def process1_socket(self, port):
        host = '127.0.0.1'
        port = 5002
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        return s

    def process1_events(self, process_port):
        self.events_sent = [2.1, 2.2, 2.3]
        self.flag = False
        self.process_port = int(process_port)
        self.sock = self.makeserverport(self.process_port)
        self.events = []
        self.ack = []

    def process1_send(self):
        while self.flag is False:
            message1 = {'message': 2.1}
            message2 = {'message': 2.2}
            message3 = {'message': 2.3}
            self.sock.sendto(str(message1).encode('utf-8'), ('host', 5001))
            self.sock.sendto(str(message2).encode('utf-8'), ('host', 5001))
            self.sock.sendto(str(message3).encode('utf-8'), ('host', 5001))
            self.sock.sendto(str(message1).encode('utf-8'), ('host', 5003))
            self.sock.sendto(str(message2).encode('utf-8'), ('host', 5003))
            self.sock.sendto(str(message3).encode('utf-8'), ('host', 5003))

    def process1_listen(self):
        while true:
            try:
                if self.sock is not None:
                    data, server_address = self.sock.recvfrom(1024)
                    decode_data = eval(data.decode('utf-8'))
                    if 'message' in decode_data:
                        self.events_sofar.append(decode_data['message'])
                    elif 'ack' in decode_data:
                        self.ack_recv.append(decode_data['ack'])
            except KeyboardInterrupt:
                self.sock.close()

    def process1_ack(self):
        if len(self.events_sofar) > 0:
            self.events_sofar = sorted(self.events_sofar)
            for each_event in range(len(self.events_sofar)):
                fractional, pid = math.modf(self.events_sofar[each_event])
                if pid == 1:
                    self.sock.sendto(str({'ack': self.events_sofar[each_event]}).encode('utf-8'), ('host', 5001))
                elif pid == 3:
                    self.sock.sendto(str({'ack': self.events_sofar[each_event]}).encode('utf-8'), ('host', 5003))

    def process1_observe(self):
        while True:
            if len(self.ack_recv) > 0:
                set.flag = True
                break
            else:
                continue

    def print_events(self):
        for event in range(len(self.events_sent)):
            self.events_sofar.append(self.events_sent[event])
        b = list(set(self.events_sofar))
        b.sort(key=float)
        for each in range(len(b)):
            print('successfully event {} received'.format(y[each]))


if __name__ == 'main':

    server = process2(5002)
    time.sleep(0.8)
    threading.Thread(target=server.process1_listen).start()
    threading.Thread(target=server.process1_send).start()
    threading.Thread(target=server.process1_ack).start()
    threading.Thread(target=server.process1_observe).start()
    time.sleep(4)
    server.print_events()
    print("process2-completed successfully")
