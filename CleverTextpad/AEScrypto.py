import pyAesCrypt
import random
import os

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024

_seed = random.randrange(0, 255, 1)

password = "foopassword"


def generate_key(_seed, _password):
    key = ""
    for i in _password:
        key += chr(ord(i) ^ _seed)
    #print(bin(key))
    print(key)
    final = ' '.join(format(ord(x), 'b') for x in key)
    print(bin(_seed))
    print(final)
    return key


def infer_key(_seed, raw):

    result = ""

    for i in raw:
        result += chr(ord(i) ^ _seed)

    print(result)
    pass


"""w = generate_key(_seed, password)

infer_key(_seed, w)
f = open("texts/dontdeletethis.txt", "w+")
f.write(str(_seed))
f.close()
os.system("attrib +h texts/dontdeletethis.txt")"""


# encrypt
def AESsave (original, encrypted, key, bufferSize):
    pyAesCrypt.encryptFile(original, encrypted, key, bufferSize)
    """OGname = split[0]
    OGname += "_seed.txt"
    final = os.path.join('texts/', OGname)
    f = open(final, "w+")
    f.write(str(_seed))
    f.close()
    os.system("attrib +h " + final)"""
    pass


def AESopen (raw, decrypted, key, bufferSize):
    pyAesCrypt.decryptFile(raw, decrypted, key, bufferSize)
    """base = os.path.basename(raw)
    split = os.path.splittext(base)
    OGname = split[0]
    OGname += "_seed.txt"
    final = os.path.join('texts/', OGname)
    f = open(final, "w+")
    f.read()
    f.close()"""
    pass


#pyAesCrypt.encryptFile("texts/data.txt", "texts/data.txt.aes", w, bufferSize)
# decrypt
#pyAesCrypt.decryptFile("texts/data.txt.aes", "texts/dataout.txt", w, bufferSize)