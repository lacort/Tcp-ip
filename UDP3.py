import socket
import sys, select
#import array
#import ipaddress
from time import sleep


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.setblocking(True)
s.bind(('', 2106))

send_address = ('255.255.255.255', 2102)
strtext = 'SETUP'
s.sendto(strtext.encode(), send_address)


while 1:
    try:
        message, address = s.recvfrom(8192)
        if message:
            strIpAddress = ''
            strMask = ''
            strGateway = ''
            strMac = ''

            for temp in message[14:18]:
                strIpAddress = strIpAddress + str(temp) + '.'
            strIpAddress = strIpAddress.rstrip('.')

            for temp in message[4:8]:
                strMask = strMask + str(temp) + '.'
            strMask = strMask.rstrip('.')

            for temp in message[:4]:
                strGateway = strGateway + str(temp) + '.'
            strGateway = strGateway.rstrip('.')

            for temp in message[8:14]:
                strMac = strMac + hex(temp).replace('0x', '').upper() + ':'
            strMac = strMac.rstrip(':')

            print('IP:      {}\nMask:    {}\nGateway: {}\nMac:     {}'.format(strIpAddress, strMask, strGateway, strMac))
            config = str(input('\nDeseja configurar [S/N]: ')).upper()
            while 1:
                try:
                    if config == 'S':
                        strChoiceIpAddress = str(input('Digite o IP que quer configurar: '))
                        while 1:
                            try:
                                if strChoiceIpAddress == strIpAddress:
                                    strNewIpAddress = str(input('Digite o novo IP: '))
                                    strNewMask = str(input('Digite a Máscara: '))
                                    if strNewMask =='':
                                        strNewMask = strMask

                                    strNewGateway = str(input('Digite o Gateway: '))
                                    if strNewGateway == '':
                                        strNewGateway = strGateway
                                    strNewMac = str(input('Digite o MacAddress: '))
                                    if strNewMac == '':
                                        strNewMac = strMac
                                    strNewIpAddress = strNewIpAddress.replace('.', ' ').split()
                                    strNewMask = strNewMask.replace('.', ' ').split()
                                    strNewGateway = strNewGateway.replace('.', ' ').split()
                                    strNewMac = strNewMac.replace(':', ' ').split()
                                    print('Processing...\n')
                                    p1 = 0
                                    p2 = 0
                                    list1 = []
                                    for temp in strNewIpAddress[:4]:
                                        p1 = p1 + int(temp)
                                        p2 = int(temp)
                                        list1.append(p2)

                                    list2 = []
                                    for temp in strNewMask[:4]:
                                        p1 = p1 + int(temp)
                                        p2 = int(temp)
                                        list2.append(p2)

                                    list3 = []
                                    for temp in strNewGateway[:4]:
                                        p1 = p1 + int(temp)
                                        p2 = int(temp)
                                        list3.append(p2)

                                    list4 = []
                                    for temp in strNewMac[:6]:
                                        p1 = p1 + int(temp, 16)
                                        p2 = int(temp, 16)
                                        list4.append(p2)

                                    n = bytearray(message)
                                    n[17] = list1[3]
                                    n[16] = list1[2]
                                    n[15] = list1[1]
                                    n[14] = list1[0]

                                    n[7] = list2[3]
                                    n[6] = list2[2]
                                    n[5] = list2[1]
                                    n[4] = list2[0]

                                    n[3] = list3[3]
                                    n[2] = list3[2]
                                    n[1] = list3[1]
                                    n[0] = list3[0]


                                    n[13] = list4[5]
                                    n[12] = list4[4]
                                    n[11] = list4[3]
                                    n[10] = list4[2]
                                    n[9]  = list4[1]
                                    n[8]  = list4[0]

                                    resposta = 'CHANGE'.encode() + message[8:14] + n
                                    s.sendto(resposta, send_address)
                                    sleep(4)
                                    s.sendto(strtext.encode(), send_address)

                                    break
                                else:
                                    print('\nEscolha um IP valido!!\n')
                                    strChoiceIpAddress = str(input('Digite o IP que quer configurar: '))
                            except Exception as ve:

                                print(ve)
                        break
                    else:
                        print('\n\033[1;4;31mEscolha S para configurar !!\033[m')
                        config = str(input('\nDeseja configurar [S/N]: ')).upper()
                except Exception as ve:
                    print(ve)
    except:
        pass