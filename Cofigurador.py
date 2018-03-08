import socket
from ModuloUtils import *
import threading
from spider_utils import ModuloSpider
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
send_address = ('255.255.255.255', 2102)
s.setblocking(True)
s.bind(('', 2106))


listM = []
listModules = []

def atualizarLista():
    try:
        listModules.clear()
        listM.clear()
        send_address = ('255.255.255.255', 2102)
        strtext = 'SETUP'
        s.sendto(strtext.encode(), send_address)
        sleep(0.5)
    except Exception as se:
        pass

    return listModules

def ThreadRecive():
    while 1:
        message, address = s.recvfrom(8192)
        listModules.append(message)
        strIpAddress = splitFields(message, 'Ip')
        strMac = splitFields(message, 'Mac')
        strVersion = splitFields(message, 'Version')
        print('{})IP: {}   Mac: {}   Versão: {}'.format(len(listModules), strIpAddress, strMac, strVersion))

def ConfigModule():
    strIp = str(input('Digite o Ip: '))
    if strIp == '':
        m.strIpAddress = m.strIpAddress
    else:
        m.strIpAddress = strIp

    strMask = str(input('Digite a Máscara: '))
    if strMask == '':
        m.strMask = m.strMask
    else:
        m.strMask = strMask

    strGateway = str(input('Digite o Gateway: '))
    if strGateway == '':
        m.strGateway = m.strGateway
    else:
        m.strGateway = strGateway

    strMac = str(input('Digite o Mac: '))
    if strMac == '':
        m.strMac = m.strMac
    else:
        m.strMac = strMac

    strBaud = str(input('Digite o BaudRate: '))
    if strBaud == '':
        m.strBaud = m.strBaud
    else:
        m.strBaud = strBaud

    strPort = str(input('Digite o Porta: '))
    if strPort == '':
        m.strPort = m.strPort
    else:
        m.strPort = strPort

    strName = str(input('Digite o Nome: ')).ljust(10)
    if strName == '          ':
        m.strName = m.strName
    else:
        m.strName = strName

t = threading.Thread(target=ThreadRecive)
t.daemon = True
t.start()

while 1:
    select1 = str(input('\nDigite [A] para atualizar Lista ou [C] para configurar : ')).upper()

    if select1 == 'A':
        print()
        listM = atualizarLista()
        sleep(1)

    elif select1 == 'C':
        select2 = str(input('Escolha o Módulo para configurar: '))
        select3 = listM[int(select2)-1]

        if select3:
            m = ModuloSpider(select3)
            print('\nIp:       {}\nMáscara:  {}\nGateway:  {}'
                  '\nMac:      {}\nBaudRate: {}\nPorta:    {}\nNome:     {}'.format(m.strIpAddress, m.strMask, m.strGateway, m.strMac, m.strBaud, m.strPort, m.strName))

            ConfigModule()
            build = m.ChangeFrame()
            listM.clear()
            print()

            s.sendto(build, send_address)
            sleep(4)
            print()
            atualizarLista()