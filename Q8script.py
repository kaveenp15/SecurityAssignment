import hashlib
import sys
import random
import string

def my_string(v = 10):
    return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(v))

salt = my_string()

value = (sys.argv[1])

hashValue = hashlib.sha512(salt.encode() + value.encode())
hexvalue = hashValue.hexdigest()
print(hexvalue)
