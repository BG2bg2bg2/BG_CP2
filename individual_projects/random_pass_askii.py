#BG 1st

import random

def main():
    while True:
        a = input("1 = gen pass\n2 = exit")
        if a == "1":
            gen()
        elif a == "2":
            break
        else:
            print("try again")
def gen():
    a = input("how long does your pass need to be?: ")
    print(a)
    b = ackii()
    print(b)