# name = input("What's your name? ")
# if name == "Dima" :
#     print("Hey, smart-ass!")
# else:
#     print('Hello, ', name)

first = int(input('Write number: '))
second = int(input('Yet: '))
third = int(input('Give me more number!: '))
if first == (second and third):
    print(3)
elif first == second or third:
    print(2)
else:
    print(0)
