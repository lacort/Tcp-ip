from ModuloUtils import *
import io, json

def DictToFrame(DictModule):
  NewFrame = []

  NewFrame.extend(replyAddress(receive=DictModule['strNewGateway']))
  NewFrame.extend(replyAddress(receive=DictModule['strNewMask']))
  NewFrame.extend(replyAddress(receive=DictModule['strNewMac']))
  NewFrame.extend(replyAddress(receive=DictModule['strNewIpAddress']))
  NewFrame.extend(replyAddress(receive=DictModule['strNewBaud']))
  NewFrame.extend(replyAddress(receive=DictModule['strNewPort']))
  NewFrame.extend(replyAddress(receive=DictModule['strNewVersion']))
  NewFrame.extend([0])
  NewFrame.extend(replyAddress(receive=DictModule['strNewName']))

  bield = bytearray(NewFrame)
  return bield

def LoadModules():

  with io.open('modules.json', 'r', encoding='utf-8') as f:
      data = f.read()
  list2 = json.loads(data)

  listFrames = []
  for item in list2:
    listFrames.append(DictToFrame(item))
  return listFrames

def FrameToDict(New):
    Mac = ''
    for temp in New[6:12]:
        Mac = Mac + hex(temp).replace('0x', '').upper() + ':'
    Mac = Mac.rstrip(':')

    strGateway = splitFields2(New, 'Gateway')
    strMask = splitFields2(New, 'Mask')
    strMac = splitFields2(New, 'Mac')
    strIpAddress = splitFields2(New, 'Ip')
    strBaund = splitFields2(New, 'Baud')
    strPort = splitFields2(New, 'Port')
    #strVersion = strNewVersion
    strSocket = splitFields2(New, 'Socket')
    strName = splitFields2(New, 'Name')

    with io.open('modules.json', 'r', encoding='utf-8') as f:
        data = f.read()
    list2 = json.loads(data)


    listModules = []
    for item in list2:
        if item['strNewMac'] == Mac:

            item['strNewGateway'] = strGateway
            item['strNewMask'] = strMask
            item['strNewMac'] = strMac
            item['strNewIpAddress'] = strIpAddress
            item['strNewBaud'] = strBaund
            item['strNewPort'] = strPort
            item['strNewVersion'] = '49.49.52'
            item['strNewSocket'] = '0'
            item['strNewName'] = strName

        listModules.append(item)

    jsonModules = json.dumps(listModules)

    with io.open('modules.json', 'w', encoding='utf-8') as f:
        f.write(jsonModules)

    listModules = LoadModules()

    resosta = listModules
    return resosta