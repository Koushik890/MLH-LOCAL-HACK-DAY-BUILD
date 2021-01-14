import bcrypt

password = b"SecretPassword890c"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)