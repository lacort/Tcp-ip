import socket
from time import sleep
from ModuloUtils import splitFields, replyAddress

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

            strIpAddress = splitFields(message, 'Ip')

            strMask = splitFields(message, 'Mask')

            strGateway = splitFields(message, 'Gateway')

            strMac = splitFields(message, 'Mac')

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
                                    if strNewMask == '':
                                        strNewMask = strMask
                                    strNewGateway = str(input('Digite o Gateway: '))
                                    if strNewGateway == '':
                                        strNewGateway = strGateway
                                    strNewMac = str(input('Digite o MacAddress: '))
                                    if strNewMac == '':
                                        strNewMac = strMac

                                    print('Processing...\n')

                                    list1 = replyAddress(receive=strNewIpAddress)

                                    list2 = replyAddress(receive=strNewMask)

                                    list3 = replyAddress(receive=strNewGateway)

                                    list4 = replyAddress(receive=strNewMac)


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

                                    break
                                else:
                                    print('\nEscolha um IP valido!!\n')
                                    strChoiceIpAddress = str(input('Digite o IP que quer configurar: '))
                            except Exception as ve:

                                print(ve)
                        break
                    elif config == 'N':
                        N = str(input('Deseja reiniciar os módulos? [S/N]: ')).upper()
                        if N == 'S':
                            s.sendto(strtext.encode(), send_address)
                            break
                    else:
                        print('\n\033[1;4;31mEscolha S para configurar !!\033[m')
                        config = str(input('\nDeseja configurar [S/N]: ')).upper()
                except Exception as ve:
                    print(ve)
    except Exception as ve:
        print(ve)
