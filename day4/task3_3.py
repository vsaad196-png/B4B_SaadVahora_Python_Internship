class InvalidAgeError(Exception):
    pass

def register_user(age):
    if age<0 or age>120:
        raise InvalidAgeError('Invalid age')
    print('Registered')

try:
    register_user(130)
except InvalidAgeError as e:
    print(e)
