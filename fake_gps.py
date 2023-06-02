import socket
import threading

lines = [
    "$GPZDA,123921.00,02,06,2023,,*6B",
    "$GPRMC,123921.00,A,4744.76945,N,06442.07104,W,0.02,294.95,020623,17.4,W,D*00",
    "$GPXTE,A,A,,L,N,D*18",
    "$GPBOD,,T,,M,,*47",
    "$GPGGA,123922.00,4744.76945,N,06442.07104,W,2,10,1.1,10.1,M,-21.2,M,5.0,0131*4D",
    "$GPVTG,304.53,T,321.91,M,0.02,N,0.03,K,D*2E",
    "$GPZDA,123922.00,02,06,2023,,*68",
    "$GPRMC,123922.00,A,4744.76945,N,06442.07104,W,0.02,304.53,020623,17.4,W,D*01",
    "$GPXTE,A,A,,L,N,D*18",
    "$GPBOD,,T,,M,,*47",
    "$GPGGA,123923.00,4744.76946,N,06442.07104,W,2,10,1.1,10.2,M,-21.2,M,6.0,0131*4F",
    "$GPVTG,327.39,T,344.76,M,0.02,N,0.04,K,D*2E",
    "$GPZDA,123923.00,02,06,2023,,*69",
    "$GPRMC,123923.00,A,4744.76946,N,06442.07104,W,0.02,327.39,020623,17.4,W,D*0E",
    "$GPXTE,A,A,,L,N,D*18",
    "$GPBOD,,T,,M,,*47",
    "$GPGGA,123924.00,4744.76946,N,06442.07104,W,2,10,1.1,10.2,M,-21.2,M,7.0,0131*49",
    "$GPVTG,334.40,T,351.77,M,0.01,N,0.02,K,D*22",
    "$GPZDA,123924.00,02,06,2023,,*6E",
    "$GPRMC,123924.00,A,4744.76946,N,06442.07104,W,0.01,334.40,020623,17.4,W,D*06",
    "$GPXTE,A,A,,L,N,D*18",
    "$GPBOD,,T,,M,,*47",
    "$GPGGA,123925.00,4744.76946,N,06442.07104,W,2,10,1.1,10.2,M,-21.2,M,7.0,0131*48",
    "$GPVTG,338.39,T,355.77,M,0.01,N,0.03,K,D*25",
    "$GPZDA,123925.00,02,06,2023,,*6F",
    "$GPRMC,123925.00,A,4744.76946,N,06442.07104,W,0.01,338.39,020623,17.4,W,D*05",
    "$GPDTM,W84,,0.0,N,0.0,E,0.0,W84*6F",
    "$GPBOD,,T,,M,,*47",
    "$GPXTE,A,A,,L,N,D*18",
    "$GPGGA,123926.00,4744.76946,N,06442.07103,W,2,10,1.1,10.2,M,-21.2,M,7.0,0131*4C",
    "$GPVTG,355.48,T,12.86,M,0.01,N,0.02,K,D*17",
    "$GPZDA,123926.00,02,06,2023,,*6C",
    "$GPRMC,123926.00,A,4744.76946,N,06442.07103,W,0.01,355.48,020623,17.4,W,D*0C",
    "$GPXTE,A,A,,L,N,D*18",
    "$GPBOD,,T,,M,,*47",
]

UDP_IP = "127.0.0.1"
UDP_PORTS = [4001, 4002, 4003]

msg_count = len(lines)
i = 0


def sendmsg():
    global i
    threading.Timer(1, sendmsg).start()
    msg = lines[i % msg_count]
    i += 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    for UDP_PORT in UDP_PORTS:
        sock.sendto(msg.encode('ascii'), (UDP_IP, UDP_PORT))
    print(msg)


sendmsg()
