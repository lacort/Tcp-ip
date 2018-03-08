

import socket
from tkinter import *
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
send_address = ('255.255.255.255', 2102)
s.settimeout(0.5)
s.bind(('', 2106))
listM = []
listModules = []

janela = Tk()
janela.title('Módulo TCP-IP')


def atualizarLista():
    listModules.clear()
    send_address = ('255.255.255.255', 2102)
    strtext = 'SETUP'
    s.sendto(strtext.encode(), send_address)
    cont = 1

    while 1:
        try:
            message, address = s.recvfrom(8192)
            listModules.append(message)
            strIpAddress = splitFields(message, 'Ip')
            strMac = splitFields(message, 'Mac')
            strVersion = splitFields(message, 'Version')
            print('{})IP: {}   Mac: {}   Versão: {}'.format(cont, strIpAddress, strMac, strVersion))
            cont = cont + 1
        except Exception as se:
            if str(se) == 'timed out':
                break
    return listModules

def splitFields(message, field):
    if field == 'Ip':
        Ip = ''
        for temp in message[14:18]:
            Ip = Ip + str(temp) + '.'
        Ip = Ip.rstrip('.')
        return Ip

    if field == 'Mask':
        Mask = ''
        for temp in message[4:8]:
            Mask = Mask + str(temp) + '.'
        Mask = Mask.rstrip('.')
        return Mask

    if field == 'Gateway':
        Gateway = ''
        for temp in message[:4]:
            Gateway = Gateway + str(temp) + '.'
        Gateway = Gateway.rstrip('.')
        return Gateway

    if field == 'Mac':
        Mac = ''
        for temp in message[8:14]:
            Mac = Mac + hex(temp).replace('0x', '').upper() + ':'
        Mac = Mac.rstrip(':')
        return Mac

    if field == 'Baund':
        Baund = ''
        for temp in message[18:20]:
            Baund = Baund + str(temp) + '.'
        Baund = Baund.rstrip('.')
        return Baund

    if field == 'Port':
        Port = ''
        for temp in message[20:22]:
            Port = Port + str(temp) + '.'
        Port = Port.rstrip('.')
        return Port


    if field == 'Version':
        Version = chr(message[22])
        Version += '.'
        Version += chr(message[23])
        Version += chr(message[24])
        return Version

    if field == 'Socket':
        Socket = int(message[25])
        return Socket


    if field == 'Name':
        Name = ''
        for temp in message[26:36]:
            Name+= chr(temp)
        return Name

'''def replyAddress(receive):
    p1 = 0
    p2 = 0
    listReceive = []
    if receive.count('.') == 3:
        receive = receive.split('.')

        for temp in receive[:4]:
            p1 = p1 + int(temp)
            p2 = int(temp)
            listReceive.append(p2)
        return listReceive

    elif receive.count('.')==2:
        receive = receive.split('.')
        for temp in receive[:3]:
            p1 = p1 + int(temp)
            p2 = int(temp)
            listReceive.append(p2)
        return listReceive

    elif receive.count('.')==1:
        receive = receive.split('.')
        for temp in receive[:2]:
            p1 = p1 + int(temp)
            p2 = int(temp)
            listReceive.append(p2)
        return listReceive

    #elif receive.count('.')==0:

        #for temp in receive[:1]:
           #p1 = p1 + int(temp)
            #p2 = int(temp)
            #listReceive.append(p2)
        #return listReceive


    elif receive.count(':') == 5 :
        receive = receive.split(':')
        for temp in receive[:6]:
            p1 = p1 + int(temp, 16)
            p2 = int(temp, 16)
            listReceive.append(p2)
        return listReceive

    elif receive.count('.')==9:
        receive = receive.split('.')
        for temp in receive[:10]:
            p1 = p1 + int(temp)
            p2 = int(temp)
            listReceive.append(p2)
        return listReceive

def splitFields2(message, field):
    if field == 'Ip':
        Ip = ''
        for temp in message[26:30]:
            Ip = Ip + str(temp) + '.'
        Ip = Ip.rstrip('.')
        return Ip

    if field == 'Mask':
        Mask = ''
        for temp in message[16:20]:
            Mask = Mask + str(temp) + '.'
        Mask = Mask.rstrip('.')
        return Mask

    if field == 'Gateway':
        Gateway = ''
        for temp in message[12:16]:
            Gateway = Gateway + str(temp) + '.'
        Gateway = Gateway.rstrip('.')
        return Gateway

    if field == 'Mac':
        Mac = ''
        for temp in message[20:26]:
            Mac = Mac + hex(temp).replace('0x', '').upper() + ':'
        Mac = Mac.rstrip(':')
        return Mac

    if field == 'Baund':
        Baund = ''
        for temp in message[30:32]:
            Baund = Baund + str(temp) + '.'
        Baund = Baund.rstrip('.')
        return Baund

    if field == 'Port':
        Port = ''
        for temp in message[32:34]:
            Port = Port + str(temp) + '.'
        Port = Port.rstrip('.')
        return Port

    if field == 'Socket':
        Socket = str(message[34])
        return Socket

    if field == 'Name':
        Name = ''
        for temp in message[35:45]:
            Name += str(temp) + '.'
        Name = Name.rstrip('.')
        return Name

def ConvertChrToStr(message, field):
    if field == 'Name':
        Name = ''
        for temp in message[26:36]:
            Name += str(temp) + '.'
        Name = Name.rstrip('.')
        return Name

    if field == 'Name2':
        Name = ''
        Convert = ''
        Name2 = ''
        for temp in message:
            Name = Name + temp
            Convert = ord(temp)
            Name2 = Name2 + str(Convert) + '.'
        Name2 = Name2.rstrip('.')
        return Name2

    if field == 'Port':
        p1=''
        p2=''

        Port = ''

        for temp in message:
            p1 = p1 + temp
            p2 = hex(temp)
            Port = Port.append(p2)

        return Port

def ModuleReader():
    strIpAddress = splitFields(select3, 'Ip')
    strMask = splitFields(select3, 'Mask')
    strGateway = splitFields(select3, 'Gateway')
    strMac = splitFields(select3, 'Mac')
    strBaund = splitFields(select3, 'Baund')
    if strBaund == '9.96':
        strBaund = '2400'

    elif strBaund == '18.192':
        strBaund = '4800'

    elif strBaund == '37.128':
        strBaund = '9600'

    elif strBaund == '75.0':
        strBaund = '19200'

    elif strBaund == '225.0':
        strBaund = '57600'
    strPort = splitFields(select3, 'Port')
    strName = splitFields(select3, 'Name')

    print('\nIp:       {}\nMáscara:  {}\nGateway:  {}'
          '\nMac:      {}\nBaudRate: {}\nPorta:    {}\nNome:     {}'.format(strIpAddress,
            strMask,strGateway, strMac,strBaund, strPort,strName))

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
            if strNewBaund == '2400':
                strNewBaund = '9.96'

            elif strNewBaund == '4800':
                strNewBaund = '18.192'

            elif strNewBaund == '9600':
                strNewBaund = '37.128'

            elif strNewBaund == '19200':
                strNewBaund = '75.0'

            elif strNewBaund == '57600':
                strNewBaund = '225.0'

            if strNewBaund == '':
                strNewBaund = splitFields(select3, 'Baund')


            strNewPort = str(input('Digite a nova Porta: '))


            if strNewPort == '':
                strNewPort = splitFields(select3, 'Port')

            strNewName = str(input('Digite o novo Nome: ')).ljust(10)
            strNewName = ConvertChrToStr(strNewName,'Name2')

            if strNewName == '':
                strNewName = ConvertChrToStr(select3,'Name')

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
            print('\nVocê digitou algo errado tente novamente!!\n')'''

def bt_click():
    print('bt_click')

bt1 = Button(janela, width = 15, text = 'Atualizar', command = atualizarLista)
bt1.place(x=280, y=250)

bt2 = Button(janela, width = 15, text = 'Configurar',command = '')
bt2.place(x=280, y=280)

bt3 = Button(janela, width = 15, text = 'Configurar')
bt3.place(x=280, y=310)

lb = Label
janela.geometry('400x350+800+100')


janela.mainloop()