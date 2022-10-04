#This program will say if a number is 0, positive or negative

a = float(input("Escolha um número:"))

if a == 0:
    print("The number is 0")
elif a >= 0:
    print("The number is positive")
elif a <= 0:
    print("The number is negative")