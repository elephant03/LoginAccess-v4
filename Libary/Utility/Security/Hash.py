from argon2 import PasswordHasher, exceptions
import hashlib as h
import sys


def Hash(Text, Secure=True):
    User_String = str(Text)

    if not Secure:
        System_Encoding = sys.getfilesystemencoding()
        m = h.sha256()
        m.update(bytes(str(User_String), encoding=System_Encoding))
        Hash = m.digest()
        pass
    else:
        ph = PasswordHasher()
        Hash = ph.hash(User_String)

    return Hash


def Verify(Text, Given_Hash):
    User_String = str(Text)
    User_Hash = str(Given_Hash)

    ph = PasswordHasher()

    try:
        _Verify = ph.verify(User_Hash, User_String)
        Pass = True
    except exceptions.VerifyMismatchError:
        Pass = False

    return Pass


if __name__ == "__main__":
    '''
    while True:
        Go = str(input("HASH VERIFY OR QUIT\n")).lower()
        if Go == "quit":
            raise SystemExit
        elif Go == "hash":
            String = str(input("Please enter your string to hash: "))

            print(Hash(String, Secure=True))

        elif Go == "verify":
            Hash = str(input("Please enter the hash: "))
            String = str(input("Please enter the comparason string: "))

            print(Verify(String, Hash))

        else:
            pass
    '''
    print(str(Hash("student", Secure=False)))
