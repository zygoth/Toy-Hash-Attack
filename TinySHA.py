import hashlib
import random

hashCounter = random.randint(-10000000, 10000000)

def getTinySHA1(numBits):

    global hashCounter
    m = hashlib.sha1()
    m.update(str(hashCounter))
    b = bytearray(m.hexdigest())
    hashCounter += 1
    return b[0:numBits/4]    

def getCurrentSeed():

    global hashCounter
    return str(hashCounter)
