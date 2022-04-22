import random
import string


def is_name_valid(name: str) -> bool:
    if not name:
        return False

    for char in name:
        if not (("A" <= char <= "Z") or ("a" <= char <= "z") or (char == " ")):
            return False
    return True


def is_account_valid(account_no: str) -> bool:
    if not account_no:
        return False

    if len(account_no) == 16 and account_no.isdecimal():
        return True
    return False


def generate_random_account_no(digit_len=16):
    return ''.join(random.choices(string.digits, k=digit_len))
