import rsa
import os.path

pbKeyFile = "rsaKeys/public_key.pem"
pvKeyFile = "rsaKeys/private_key.pem"


def saveToFile():
    if not os.path.isfile(pbKeyFile) and not os.path.isfile(pvKeyFile):
        print('[*] Generating secret, please hang on.')
        publicKey, privateKey = rsa.newkeys(2048)

        publicFile = open(pbKeyFile, "wb")
        publicFile.write(publicKey.save_pkcs1("PEM"))
        publicFile.close()

        privateFile = open(pvKeyFile, "wb")
        privateFile.write(privateKey.save_pkcs1("PEM"))
        privateFile.close()
        print("[*] Keys have been stored")
    else:
        print("[*] Keys already exist")


def importPublicKey():
    with open(pbKeyFile, "rb") as file:
        key = rsa.PublicKey.load_pkcs1(file.read(), "PEM")
    return key


def importPrivateKey():
    with open(pvKeyFile, "rb") as file:
        key = rsa.PrivateKey.load_pkcs1(file.read(), "PEM")
    return key


def encrypt(msg: str):
    return rsa.encrypt(msg.encode(), importPublicKey())


def decrypt(msg):
    return rsa.decrypt(msg, importPrivateKey()).decode()
