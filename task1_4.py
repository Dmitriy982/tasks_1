n = int(input("Введите число n: "))
b = 0
while n:
    a = n % 10
    if a > b:
        b = a
    n = n // 10
print(f"Наибольшая цифра в числе n: {b}")

