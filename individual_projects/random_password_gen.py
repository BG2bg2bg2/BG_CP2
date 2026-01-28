#BG 1st random password generator

#import libraires
import random

#global variables
password = []
upper = ["A", "B", "C", "D","E","F","G","H",'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower = ["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['1','2','3','4','5','6','7','8','9','0']
special = ["`",'~','!','@','#','$','%','^','&','*','(',')','_','+','-','=',"'",'"',';',':','<','>','.','?','/',',','[',']','\\','|','}','{','}']
z = []
#main Function that runs the code
def main():
    while True:
        passes = input("Enter a number 1 to generate pass \n2 to exit:")
        if passes == "1":
            gen()
        elif passes =="2":
            break
        else:
            print("Try again")
#function for the different password requirements
def gen():
    while True:
        #user specifies the length and if they want to include
        a = input("How long does the pass need to be: ")
        if a >= "8":
            #funtion for uppercase letters
            b = input("Do you need uppercase Y/N: ")
            c = input("Do you need lowercase Y/N: ")
            d = input("Do you need number letters Y/N: ")
            e = input("Do you need special characters letters Y/N: ")
            if b == "y":
                f = True
            elif b == "n":
                f = False

            if c == "y":
                g = True
            elif c == "n":
                g = False

            if d == "y":
                h = True
            elif d == "n":
                h = False

            if e == "y":
                i = True
            elif e == "n":
                i = False

            return b, c, d, e
        else:
            print("Try again")
            continue
#function that assembles the password once it is the correct length
def what(b,c,d,e):
    

    
    #function for lowercase letters
    #numbers
    #special characters



#How long does the password need to be: 12

#Does the password need lowercase letters (Y/N): Y

#Does the password need uppercase letters (Y/N): N

#Does the password need numbers letters (Y/N): Y

#Does the password need special characters letters (Y/N): Y

#Possible Passwords:

#k7#9xm2$pq3f

#3j@vn8b5zr&t

#p4%qw9y6m$2c

#f8!2nh6l@x7d
main()