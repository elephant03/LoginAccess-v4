def Hash(Text):
    User_String = str(Text)
    Hash = pwd_context.hash(User_String)

    return Hash


def Verify(Text, Given_Hash):
    User_String = str(Text)
    User_Hash = str(Given_Hash)
    Verify = pwd_context.verify(User_String, User_Hash)

    return Verify


if __name__ == "__main__":
    from Context import pwd_context

    while True:
        Go = str(input("HASH VERIFY OR QUIT\n")).lower()
        if Go == "quit":
            raise SystemExit
        elif Go == "hash":
            String = str(input("Please enter your string to hash: "))

            print(Hash(String))

        elif Go == "verify":
            Hash = str(input("Please enter the hash: "))
            String = str(input("Please enter the comparason string: "))

            print(Verify(String, Hash))

        else:
            pass

else:
    from Libary.Security.Context import pwd_context
