import simple_colors
from simple_colors import *
# Dumb calc
run = True
print(green("Hi, this's my first calculator ",['bold', 'underlined']))
print(green("Let's choose an action",['bright']))
print(green("If you want to choose +, type: + .",['italic']))
print(green("If you want to choose -, type: - .",['italic']))
print(green("If you want to choose *, type: * .",['italic']))
print(green("If you want to choose /, type: / .",['italic']))
print(green("If you want to raise the number to the degree of 2, type 2 .",['italic']))
print(green("If you want to raise the number to any degree, type n .",['italic']))
what = input(green("Chose the action: ",['italic']))
def action():
    print(green("Want to continue this action?"))
def answer():
    print(green("Your answer is: ",['underlined']))
def GOOD():
    print(green("GOOD"))
def BYE():
    print(red("Thanks, BYE!"))
def wrong():
    print(red("Wrong sign!", ['italic', 'bright','underlined']))
while run:
    if what == "+":
        a = float(input(green("Enter first number: ")))  ## переводимо текст в число щоб виконувати дії
        b = float(input(green("Enter second number: ")))
        answer()
        print(cyan(str(a + b)))    ## ЩОБ КОЛО ТЕКСТУ ПИСАТИ ДІЇ + str(дія або число)
        action()
        s = input(green("yes/no : "))
        if s == "no":
            BYE()
            break
        elif s == "yes":
            GOOD()
        else:
            wrong()
            break
    elif what == "n":
        a = float(input(green("Enter first number: ")))
        b = float(input(green("Enter second number: ")))
        if a > 100:                            ##Функція в функції
            print(green("Wow big 1number"))
        if b > 100:
            print(green("Wow 2nd number is big xD"))
        if a < 100:
            print(green("Interesting one"))
        print(green("{} To the degree of {} is: ".format(a, b))) #FORMAT ДУЖЕ ВАЖЛИВО
        print(cyan(str(a ** b),['underlined']))
        action()
        s = input(green("yes/no : "))
        if s == "no":
            BYE()
            break
        elif s == "yes":
            GOOD()
        else:
            wrong()
            break
    elif what == "2":
        a = float(input(green("Enter your number: ")))
        print(green("Square of " + str(a) + " is "))
        print(cyan(str(a ** 2),['underlined']))
        action()
        s = input(green("yes/no : "))
        if s == "no":
            BYE()
            break
        elif s == "yes":
            GOOD()
        else:
            wrong()
    elif what == "-":
        a = float(input(green("Enter first number: ")))  ## переводимо текст в число щоб виконувати дії
        b = float(input(green("Enter second number: ")))
        answer()
        print(cyan(str(a - b), ['underlined']))
        action()
        s = input(green("yes/no : "))
        if s == "no":
            BYE()
            break
        elif s == "yes":
            GOOD()
        else:
            wrong()
            break
    elif what == "*":
        a = float(input(green("Enter first number: ")))  ## переводимо текст в число щоб виконувати дії
        b = float(input(green("Enter second number: ")))
        answer()
        print(cyan(str(a * b), ['underlined']))
        action()
        s = input(green("yes/no : "))
        if s == "no":
            BYE()
            break
        elif s == "yes":
            GOOD()
        else:
            wrong()
            break
    elif what == "/":
        a = float(input(green("Enter first number: ")))  ## переводимо текст в число щоб виконувати дії
        b = float(input(green("Enter second number: ")))
        answer()       
        print(cyan(str(a / b), ['underlined']))
        action()
        s = input(green("yes/no : "))
        if s == "no":
            BYE()
            break
        elif s == "yes":
            GOOD()
        else:
            wrong()
            break
    else:
        wrong()
        break
print(cyan("The END!",['italic', 'underlined']))