import string
import random

# characters to generate password
char = list(string.ascii_letters + string.digits + "!@#$%^&*()_")


def gen_random_pass():
    length = int(input("Enter password length: "))  # length of password from the user
    random.shuffle(char)  # Shuffling the characters
    password = []  # picking random characters from the list
    for i in range(length):
        password.append(random.choice(char))

    random.shuffle(password)  # Shuffling the resultant password
    print("".join(password))  # converting list into string & printing the list


gen_random_pass()  # invoking the function