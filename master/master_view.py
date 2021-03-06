import os

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto import Random


def decrypt_valuables(f):
    # TODO: For Part 2, you'll need to decrypt the contents of this file
    # The existing scheme uploads in plaintext
    # As such, we just convert it back to ASCII and print it out

    # Import the private key from the root folder of Master
    private_key = RSA.importKey(open('mykeyprivate.pem').read())
    dsize = SHA.digest_size
    sentinel = Random.new().read(15+dsize)
    cipher = PKCS1_v1_5.new(private_key)
    # Decrypt the message with the key
    encoded_text = cipher.decrypt(f, sentinel)
    decoded_text = encoded_text.decode("ascii")

    print(decoded_text)


if __name__ == "__main__":
    fn = input("Which file in pastebot.net does the botnet master want to view? ")
    if not os.path.exists(os.path.join("../pastebot.net", fn)):
        print("The given file doesn't exist on pastebot.net")
        os.exit(1)
    f = open(os.path.join("../pastebot.net", fn), "rb").read()
    decrypt_valuables(f)
