from bcrypt import hashpw, gensalt

hashed = hashpw('1234567', gensalt())
print(hashed)
if hashpw('123456', hashed) == hashed:
    print('it maches')
else:
    print('it does not match')
