import socket
import threading

with open("CAR-2021-014-002.pnmea") as file:
    lines = file.readlines()

UDP_IP = "127.0.0.1"
UDP_PORT = 5001

msg_count = len(lines)
i = 0

def sendmsg():
    global i
    threading.Timer(1, sendmsg).start()
    msg = lines[i % msg_count]
    i += 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    sock.sendto(msg.encode('ascii'), (UDP_IP, UDP_PORT))
    print(msg)

sendmsg()
