a = int(input("Введите десятичное число: "))

dvoich = bin(a)[2:]

vosmirich = oct(a)[2:]

print(f"Двоичная СС: {dvoich}")
print(f"Восьмеричная СС: {vosmirich}")