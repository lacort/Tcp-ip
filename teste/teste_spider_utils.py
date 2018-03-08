from spider_utils import ModuloSpider
import socket
Frame =  b'\xc0\xa8\x01\x01\xff\xff\xff\x00@\xd8U\x19\x08\xaa\xc0\xa8\x01W\t`\x085114\x00Jefferson1'
Frame2 = b'\xc0\xa8\x01\x01\xff\xff\xff\x00"3DUfw\xc0\xa8\x01W\t`\x085114\x00Jefferson1'
Frame3 = b'\xc0\xa8\x01\x01\xff\xff\xff\x00\x113DUfw\xc0\xa8\x01W\t`\x085114\x00Jefferson1'
Frame4 = b'\xc0\xa8\x01\x01\xff\xff\xff\x00@\xd8U\x19\x08\xab\xc0\xa8\x01W\t`\x085114\x00Jefferson1'
m = ModuloSpider()

print('Ip: {}  Mask: {}  Gateway: {}  Mac: {}  Baund: {}  Porta: {}  Versão: {}  Nome: {}'.format(m.strIpAddress, m.strMask, m.strGateway, m.strMac, m.strBaud, m.strPort,m.strVersion, m.strName))


m.strPort ='1010'

m.ChangeFrame()

print(m.ToFrame())


print('Ip: {}  Mask: {}  Gateway: {}  Mac: {}  Baund: {}  Porta: {}  Versão: {}  Nome: {}'.format(m.strIpAddress, m.strMask, m.strGateway, m.strMac, m.strBaud, m.strPort,m.strVersion, m.strName))

