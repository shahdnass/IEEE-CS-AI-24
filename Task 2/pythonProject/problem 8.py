import secrets
import string


def generate_password():

    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(8))
    return password

password = generate_password()
print("Random Password:", password)
