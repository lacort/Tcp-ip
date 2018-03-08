class ModuloSpider():

    def __init__(self, Frame = None):
        if Frame != None:
            self.ConvertFromByteArrayStr(Frame)
            self.strVersion1 = Frame[22:25]
            self.__originalMac = Frame[8:14]
        else:
            self.strIpAddress = '127.0.0.1'
            self.strMask = '255.255.255.0'
            self.strGateway = '0.0.0.0'
            self.strMac = '00:50:AA:12:09:AB'
            self.strBaud = '4800'
            self.strPort = '2101'
            self.strVersion = '3.11'
            self.strName = 'Teste     '
            self.__Mac = self.replyAddress(receive=self.strMac)
            self.__originalMac = bytearray(self.__Mac)


        pass

    def ConvertFromByteArrayStr(self, frame):
        self.strIpAddress = self.splitFields(frame, 'Ip')
        self.strMask = self.splitFields(frame, 'Mask')
        self.strGateway = self.splitFields(frame, 'Gateway')
        self.strMac = self.splitFields(frame, 'Mac')
        self.strBaud = self.splitFields(frame, 'Baud')
        self.strPort = self.splitFields(frame, 'Port')
        self.strVersion = self.splitFields(frame, 'Version')
        self.strName = self.splitFields(frame, 'Name')

    def ToFrame(self):
        NewFrame = []

        NewFrame.extend(self.replyAddress(receive=self.strGateway))
        NewFrame.extend(self.replyAddress(receive=self.strMask))
        NewFrame.extend(self.replyAddress(receive=self.strMac))
        NewFrame.extend(self.replyAddress(receive=self.strIpAddress))
        NewFrame.extend(self.replyAddress(receive=self.strBaud))
        NewFrame.extend(self.replyAddress(receive=self.strPort))
        #NewFrame.extend(self.replyAddress(receive=self.strVersion))
        NewFrame.extend([0])
        NewFrame.extend(self.ConvertNameToInt(recive=self.strName))


        bield = bytearray(NewFrame)
        return bield

    def ChangeFrame(self):
        byte = self.ToFrame()
        resposta = 'CHANGE'.encode() + self.__originalMac + byte
        return resposta

    def ConvertNameToInt(self, recive):
        Name =''
        Convert =''
        listname=[]
        for temp in recive:
            Name = Name + temp
            Convert = ord(temp)
            listname.append(Convert)
        return listname

    def splitFields(self, message, field):
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
            Baund = message[18:20]
            Baund1 = Baund[1]
            Baund1 += Baund[0] << 8
            return str(Baund1)


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

            Name=''
            for temp in message[26:36]:
                Name += chr(temp)
            return Name

    def replyAddress(self, receive):
        p1 = 0
        p2 = 0
        listReceive = []

        if receive.count('.') == 1:
            receive = receive.replace('.', '')
            for temp in receive[:3]:
                p1 = str(temp)
                p2 = ord(temp)
                listReceive.append(p2)
            return listReceive


        elif receive.count('.') == 3:
            receive = receive.split('.')

            for temp in receive[:4]:
                p1 = p1 + int(temp)
                p2 = int(temp)
                listReceive.append(p2)
            return listReceive

        elif receive.count('.') == 2:
            receive = receive.split('.')
            for temp in receive[:3]:
                p1 = p1 + int(temp)
                p2 = int(temp)
                listReceive.append(p2)
            return listReceive




        elif receive.count(':') == 5:
            receive = receive.split(':')
            for temp in receive[:6]:
                p1 = p1 + int(temp, 16)
                p2 = int(temp, 16)
                listReceive.append(p2)
            return listReceive

        elif receive.count('.') == 9:
            receive = receive.split('.')
            for temp in receive[:10]:
                p1 = p1 + int(temp)
                p2 = int(temp)
                listReceive.append(p2)
            return listReceive

        elif receive.count('.') == 0:
            Baund1 = bytearray()
            Baund1.append((int(receive) & 0xff00) >> 8)
            Baund1.append((int(receive) & 0xff))
            return Baund1
