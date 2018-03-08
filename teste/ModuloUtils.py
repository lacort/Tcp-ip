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

    if field == 'Baud':
        Baud = message[18:20]
        Baud1 = Baud[1]
        Baud1 += Baud[0] << 8
        return str(Baud1)

    if field == 'Port':
        Port = message[20:22]
        Port1 = Port[1]
        Port1 += Port[0] << 8
        return str(Port1)


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

def replyAddress(receive):
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

    elif receive.count('.')==0:
        Baund1 = bytearray()
        Baund1.append((int(receive) & 0xff00) >> 8)
        Baund1.append((int(receive) & 0xff))
        return Baund1

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

    if field == 'Baud':
        Baud = ''
        for temp in message[30:32]:
            Baud = Baud + str(temp) + '.'
        Baud = Baud.rstrip('.')
        return Baud

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




