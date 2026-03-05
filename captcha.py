import random
import string

def create_code(size=5):
    chars = string.ascii_letters + string.digits
    return "".join(random.sample(chars, size))

def check_captcha():

    code = create_code()

    print("Generated Code:", code)

    user = input("Enter the code: ")

    if user == code:
        print("Correct! Verification successful.")
    else:
        print("Wrong code. Access blocked.")

check_captcha()