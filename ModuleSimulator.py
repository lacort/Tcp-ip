from Dict import *
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.setblocking(True)
s.bind(('', 2102))

send_address = ('255.255.255.255', 2106)
#send_address = ('192.168.1.255', 2106)

while 1:
    try:
        message, address = s.recvfrom(8192)

        if message == b'SETUP':

            listModules = LoadModules()
            for item in listModules:
                s.sendto(item, send_address)

        elif len(message):

            bield = FrameToDict(message)
            for item in bield:
                s.sendto(item, send_address)
    except:
        pass