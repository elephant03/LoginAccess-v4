from passlib.context import CryptContext

pwd_context = CryptContext(

    schemes=["argon2"],

    deprecated="auto",

    argon2__rounds=1000

)
