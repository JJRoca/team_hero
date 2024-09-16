import bcrypt

def hashPassword(password: str):
    password= password.encode('utf-8')
    salt= bcrypt.gensalt()
    return bcrypt.hashpw(password,salt).decode()