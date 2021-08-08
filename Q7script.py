import hashlib
import sys
import random
import string

def random_string(v = 10):
    return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(v))

salt = random_string()

value = (sys.argv[1])

hashValue = hashlib.pbkdf2_hmac('sha512', value.encode(), salt.encode(), 200000)
hexvalue = hashValue.hex()
print(hexvalue)
