import hashlib

hashCounter = 0

def getTinySHA1(numBits):

    global hashCounter
    m = hashlib.sha1()
    m.update(str(hashCounter))
    b = bytearray(m.hexdigest())
    print(b)

    hashCounter += 1
    
getTinySHA1(16)
