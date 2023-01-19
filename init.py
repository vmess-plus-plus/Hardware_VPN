from pyDes import des, CBC, PAD_PKCS5
import urllib.request
import binascii

import uuid
import time
import sys
import os

SERVERIP = "请设置为您的服务器地址"

def des_encrypt(s, KEY):
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en).decode()

def des_descrypt(s, KEY):
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de.decode()

def checkKeyFile():
  if os.path.exists('keyfile.key'):
    return True
  else:
    return False

def getPCVmessPlusPlusUUID():
  computerUUID = uuid.uuid1()
  nowtime      = int(time.time())
  vmessplusID  = computerUUID + str(nowtime)
  return vmessplusID

def __main__():
  fileExists = checkKeyFile()
  if(not fileExists):
    print('[Error] KeyFile 不存在.')
    sys.exit(1)
  else:
    cUUID = getPCVmessPlusPlusUUID()
    if(len(cUUID) < 6):
      print('[Error] vmess++ID生成失败,请尝试切换操作系统并调整系统时钟')
      sys.exit(2)
    else:
      urllib.request.urlopen(SERVERIP + str(time.time()))
      for i in range(int(time.time()) / 10000000):
        urllib.request.urlopen(SERVERIP + "/getServerInfo")
      with open("keyfile.key","r") as f:
        key = str(f.read())
      msg = des_encrypt("getServerInfo",key)
      path = urllib.request.urlopen(SERVERIP + "/authme/api/" + str(msg))
      print(path)
