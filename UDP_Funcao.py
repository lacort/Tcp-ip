




import ipaddress



#strNewMac= '40:D8:55:19:08:AB'


def contMac (strNewMac, base):
    strNewMac = strNewMac.split(':')
    p1=0
    p2=0
    list4 = []
    for temp in strNewMac:
        p1 = p1 + int(temp,base)
        p2 = int(temp,base)
        list4.append(p2)
    return list4


listreturning =  contMac('40:D8:55:19:08:AB',16)
print(listreturning)

def splitFields (message, field):
    if field == 'Ip':
        Ip = ''
        for temp in message[14:18]:
            Ip = Ip + str(temp) + '.'
        Ip = Ip.rstrip('.')
        return Ip

    if field == 'Mac':
        Mac = ''
        for temp in message[8:14]:
            Mac = Mac + hex(temp).replace('0x', '').upper() + ':'
        Mac = Mac.rstrip(':')
        return Mac



message = b'\xc0\xa8\x01\x01\xff\xff\xff\x00\x00P\xc2\xb02N\xc0\xa8\x01\x15\xe1\x00\x085114\x0014\x0014\x0014\x00\x00'
resposta =  splitFields(message, 'Ip')
print(resposta)