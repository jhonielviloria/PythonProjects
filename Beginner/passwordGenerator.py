# Write a programme, which generates a random password for the user.
# Ask the user how long they want their password to be, and how many
# letters and numbers they want in their password. Have a mix of upper
# and lowercase letters, as well as numbers and symbols. The password
# should be a minimum of 6 characters long.
import random


def randomizer(lst, len):
    tmp = ""
    for i in range(len):
        tmp += random.choice(lst)
    return tmp


def generatePassword():
    print("Create your password here.")
    while True:
        length = int(input("input desired Length of password: "))
        ltrs_count = int(input("how many are letters: "))
        numbers_count = int(input("how many are numbers: "))
        special_count = length - ltrs_count - numbers_count
        if ltrs_count + numbers_count > length or length < 6:
            print("invalid parameters! try again")
        else:
            break

    caps_count = random.randint(1, ltrs_count - 1)
    ltrs_list = "abcdefghijklmnopqrstuvwxyz"
    numbers_list = "1234567890"
    special_list = "~!@#$%^&,.()-[]{}\/;:?"

    password = ""
    password += randomizer(ltrs_list.upper(), caps_count)
    password += randomizer(ltrs_list, ltrs_count - caps_count)
    password += randomizer(numbers_list, numbers_count)
    if special_count:
        password += randomizer(special_list, special_count)
    password = "".join(random.sample(password, len(password)))
    print(f'Your generated password is: {password}')


generatePassword()
