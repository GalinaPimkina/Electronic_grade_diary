def create_password():
    import string
    import random

    PWD_ITEMS = string.digits + string.ascii_letters + '_!><?#$&'
    pwd = ''.join([random.choice(PWD_ITEMS) for _ in range(8)])

    return pwd