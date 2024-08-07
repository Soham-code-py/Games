#!/usr/bin/python3

from random import randint       # import randint

num_1 = "string"       # Setting value for num_1 & num-2
num_2 = "string"

while True:
    num_1 = input("What is your first number: ")
    if not num_1.isdigit():                        #check if number is vailed
        print()                     #Prints new line
        print("Erorr: Not a vailed number")
        continue
    num_1 = int(num_1)   # converting str to int

    if num_1 > 1000:
        print("Error: number must be less than 1000")
    elif num_1 < -1000:
        print("Error: number must be more than -1000")
    num_2 = input("What is your second number: ")

    if not num_2.isdigit():
        print("Erorr: Not a vailed number")
        continue
    num_2 = int(num_2)   # converting str to int
    
    if num_2 > 1000:
        print("Error: number must be less than 1000")
    elif num_2 < -1000:
        print("Error: number must be more than -1000")
    if num_2 - (num_1 - 1) < 10:
        print("Error: range must be at least 10")
        continue
    else:
        break
        


def p1():
    guess = int(input("What is your guess: "))
    if guess > number:
        print("The number is lower.")          # Player 1 
        print()
    elif guess < number:
        print("The number is higher.")
        print()
    elif guess == "exit":
        exit()
    else:
        print("You Guessed right")
        print("The number was", number)
        exit()

def CPU1():
    global num_1, num_2, cpu_number
    cpu_number = randint(num_1, num_2)
    print("CPU's turn:", cpu_number)       #CPU
    print()
    if cpu_number == number:          
        print("CPU Wins!")
        print("The number was", number)
        exit()

def CPU2():
    global num_1, num_2, cpu_number
    cpu_number = randint(num_1, num_2)
    print("CPU's turn:", cpu_number)
    print()
    if cpu_number > number:
        num_2 = cpu_number - 1                 # CPU 2
    elif cpu_number < number:
        num_1 = cpu_number + 1
    else:
        print("CPU Wins!")
        print("The number was", number)
        exit()


number = randint(num_1, num_2)
guess = "str"        # Setting guess value to a number that will
cpu_number = "str"   # will not be randomized number

print("Number Generating...")          

CPU_level = input("What level would you like to use (1 or 2):")

if CPU_level == str(1):
    while True:
        p1()
        CPU1()
elif CPU_level == str(2):
    while True:
        p1()
        CPU2()
