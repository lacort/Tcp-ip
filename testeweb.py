import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
send_address = ('255.255.255.255', 2102)
s.settimeout(1)
s.bind(('', 2106))

def conectado(con, cliente):
    print('Conectado por', cliente)

    while True:
        msg = con.recv(1024)
        if not msg: break
        print(cliente, msg)

    print('Finalizando conexao do cliente', cliente)
    con.close()
    thread.exit()

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

orig = (HOST, PORT)

udp.bind(orig)
udp.listen(1)

while True:
    con, cliente = tcp.accept()
    thread.start_new_thread(conectado, tuple([con, cliente]))

udp.close()