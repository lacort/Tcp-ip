import socket
from ModuloUtils import *
from Dict import *
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
    except Exception as se:
        pass

    return listModules

def ModuleReader():

    strIpAddress = splitFields(select3, 'Ip')
    strMask = splitFields(select3, 'Mask')
    strGateway = splitFields(select3, 'Gateway')
    strMac = splitFields(select3, 'Mac')
    strBaund = splitFields(select3, 'Baund')
    strPort = splitFields(select3, 'Port')
    strName = splitFields(select3, 'Name')

    print('\nIp:       {}\nMáscara:  {}\nGateway:  {}'
          '\nMac:      {}\nBaudRate: {}\nPorta:    {}\nNome:     {}'.format(strIpAddress,
            strMask,strGateway, strMac,strBaund, strPort,strName))

def TreadRecive():
    while 1:
        message, address = s.recvfrom(8192)
        listModules.append(message)
        strIpAddress = splitFields(message, 'Ip')
        strMac = splitFields(message, 'Mac')
        strVersion = splitFields(message, 'Version')
        print('{})IP: {}   Mac: {}   Versão: {}'.format(len(listModules), strIpAddress, strMac, strVersion))

def ConfigModule():
    while 1:
        try:
            strNewIpAddress = str(input('Digite o novo IP: '))
            if strNewIpAddress == '':
                strNewIpAddress = splitFields(select3, 'Ip')

            strNewMask = str(input('Digite a nova Máscara: '))
            if strNewMask == '':
                strNewMask = splitFields(select3, 'Mask')

            strNewGateway = str(input('Digite o novo Gateway: '))
            if strNewGateway == '':
                strNewGateway = splitFields(select3, 'Gateway')

            strNewMac = str(input('Digite o novo MacAddress: '))
            if strNewMac == '':
                strNewMac = splitFields(select3, 'Mac')

            strNewBaund = str(input('Digite o novo BaudRate: '))
            if strNewBaund == '':
                strNewBaund = splitFields(select3, 'Baund')


            strNewPort = str(input('Digite a nova Porta: '))
            if strNewPort == '':
                strNewPort = splitFields(select3, 'Port')

            strNewName = str(input('Digite o novo Nome: ')).ljust(10)
            if strNewName == '          ':
                strNewName = ConvertChrToStr(select3,'Name')
            else:
                strNewName = ConvertChrToStr(strNewName, 'Name2')
            NewFrame = []

            NewFrame.extend(replyAddress(strNewGateway))
            NewFrame.extend(replyAddress(strNewMask))
            NewFrame.extend(replyAddress(strNewMac))
            NewFrame.extend(replyAddress(strNewIpAddress))
            NewFrame.extend(replyAddress(strNewBaund))
            NewFrame.extend(replyAddress(strNewPort))
            NewFrame.extend([0])
            NewFrame.extend(replyAddress(strNewName))

            bield = bytearray(NewFrame)
            return bield
        except Exception as se:
            print('\nVocê digitou algo errado tente novamente!!\n')

t = threading.Thread(target=TreadRecive)
t.daemon = True
t.start()



while 1:

    select1 = str(input('\nDigite [A] para atualizar Lista ou [C] para configurar : ')).upper()

    if select1 == 'A':
        print()
        listM = atualizarLista()
        sleep(0.2)
    elif select1 == 'C':
        select2 = str(input('Escolha o Módulo para configurar: '))
        select3 = listM[int(select2)-1]
        if select3:
            m = ModuloSpider(select3)
            print('\nIp:       {}\nMáscara:  {}\nGateway:  {}'
                  '\nMac:      {}\nBaudRate: {}\nPorta:    {}\nNome:     {}\n'.format(m.strIpAddress, m.strMask, m.strGateway, m.strMac, m.strBaud, m.strPort, m.strName))

            strIp = str(input('Digite o Ip: '))
            if strIp == '':
                m.strIpAddress = m.strIpAddress
            else:
                m.strIpAddress = strIp

            strMask = str(input('Digite a Máscara: '))
            if strMask == '':
                m.strMask =m.strMask
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

            bield = m.ChangeFrame()
            listM.clear()


            '''ModuleReader()
            bield = ConfigModule()
            resposta = 'CHANGE'.encode() + select3[8:14] + bield
            listM.clear()'''
            s.sendto(bield, send_address)
            sleep(0.2)















