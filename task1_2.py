numb = int(input("Введите число в секундах: "))
a = numb // 3600
b = numb // 60 - a * 60
c = numb % 60
print (f"{a:02}:{b:02}:{c:02}")
