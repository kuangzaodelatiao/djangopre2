# coding:utf-8
import hashlib
def md5(strs=''):
    m = hashlib.md5() # hashlib.md5(bytes('password'.encode('utf-8')))
    m.update(bytes(strs.encode('utf-8')))
    return m.hexdigest()
