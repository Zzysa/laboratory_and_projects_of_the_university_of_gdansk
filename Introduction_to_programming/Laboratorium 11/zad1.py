import numpy as np
import math

print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Modulo n")
print("6. Potęgowanie")
print("7. Pierwiastkowanie kwadratowe")
print("8. Silnia")
print("9. Logarytmowanie")
print("10. Sinus")
print("11. Cosinus")
print("12. Tangens")
print("13. Cotangens")

choice = input("Wybierz operację i wpisz jej numer: ")
num1 = float(input("Podaj pierwszą liczbę: "))

if choice == '1':
    num2 = float(input("Podaj drugą liczbę: "))
    print(np.add(num1, num2))

elif choice == '2':
    num2 = float(input("Podaj drugą liczbę: "))
    print(np.subtract(num1, num2))

elif choice == '3':
    num2 = float(input("Podaj drugą liczbę: "))
    print(np.multiply(num1, num2))

elif choice == '4':
    num2 = float(input("Podaj drugą liczbę: "))
    print(np.divide(num1, num2))

elif choice == '5':
    num2 = float(input("Podaj drugą liczbę: "))
    print(np.mod(num1, num2))

elif choice == '6':
    num2 = float(input("Podaj drugą liczbę: "))
    print(np.power(num1, num2))

elif choice == '7':
    print(np.sqrt(num1))

elif choice == '8':
    print(math.factorial(int(num1)))

elif choice == '9':
    num2 = float(input("Podaj drugą liczbę: "))
    print(np.log(num1) / np.log(num2))

elif choice == '10':
    print(np.sin(num1))

elif choice == '11':
    print(np.cos(num1))

elif choice == '12':
    print(np.tan(num1))

elif choice == '13':
    print(np.cos(num1) / np.sin(num1))
