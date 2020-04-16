# AES pycrypto package
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def EncryptPW(senha):
    # key has to be 16, 24 or 32 bytes long
    key = b'G!P@4#1$1%M4SC4D'
    iv=bytes("C#&UjO){QwzFcsPs", encoding='utf-8')
    encrypt_AES = AES.new(key, AES.MODE_CBC, iv)

    blockSize = 16

    #Mensagem que será criptografada
    message = bytes(senha, encoding='utf-8')

    ciphertext = encrypt_AES.encrypt(pad(message, blockSize))
    return base64.b64encode(ciphertext).decode("utf-8")

def DescriptografarSenha(senha):
    # Chave deverá ser identica
    blockSize = 16
    key = b'G!P@4#1$1%M4SC4D'
    iv=bytes("C#&UjO){QwzFcsPs", encoding='utf-8')
    try:
        b_senha = base64.b64decode(bytes(senha, encoding="utf-8"))
    except:
        return "Error"
    try:
        decrypt_AES = AES.new(key, AES.MODE_CBC, iv)
    except:
        return "Error"
    message_decrypted = unpad(decrypt_AES.decrypt(b_senha), blockSize)
    return message_decrypted.decode("utf-8")

   
