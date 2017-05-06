import os

from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA


def sign_file(f):
    # TODO: For Part 2, you'll use public key crypto here
    # The existing scheme just ensures the updates start with the line 'Caesar'
    # This is naive -- replace it with something better!
    # return bytes("Caesar\n", "ascii") + f
    
    key = RSA.importKey(open('mykeyprivate.pem').read())
    hash = SHA.new(f)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(hash)
    f_signed = signature + bytes("\nMessage_Start_Here\n", "ascii") + f
    return f_signed


def file_to_sign():
    fn = input("Which file in pastebot.net should be signed? ")
    if not os.path.exists(os.path.join("pastebot.net", fn)):
        print("The given file doesn't exist on pastebot.net")
        os.exit(1)
    f = open(os.path.join("pastebot.net", fn), "rb").read()
    signed_f = sign_file(f)
    signed_fn = os.path.join("pastebot.net", fn + ".signed")
    out = open(signed_fn, "wb")
    out.write(signed_f)
    out.close()
    print("Signed file written to", signed_fn)


def generate_key():
    key = RSA.generate(2048)
    f = open('mykeyprivate.pem', 'wb')
    f.write(key.exportKey('PEM'))
    f.close()

    pubkey = key.publickey()
    fv = open('mykeypublic.pem', 'wb')
    fv.write(pubkey.exportKey('PEM'))
    fv.close()


if __name__ == "__main__":

    while 1:
        print("Three commands inside:generate-key, sign, exit")
        raw_cmd = input("Enter command: ")
        cmd = raw_cmd.split()
        if not cmd:
            print("You need to enter a command...")
            continue
        if cmd[0].lower() == "generate-key":
            generate_key()
        elif cmd[0].lower() == "sign":
            file_to_sign()
        elif cmd[0].lower() == "quit" or cmd[0].lower() == "exit":
            break


