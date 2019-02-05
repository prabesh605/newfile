print("MENU \n 1=ADD \n 2=SUBSTRACT \n 3=MULTIPLY \n 4=DIVIDE \n 5=QUIT ")
ch=input("Enter your choice")
while True:
    if ch=='1':
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print(a+b)
        print("MENU \n 1=ADD \n 2=SUBSTRACT \n 3=MULTIPLY \n 4=DIVIDE \n 5=QUIT ")
        ch=input('Enter your choice')
    if ch=='2':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a - b)
        print("MENU \n 1=ADD \n 2=SUBSTRACT \n 3=MULTIPLY \n 4=DIVIDE \n 5=QUIT ")
        ch = input('Enter your choice')
    if ch=='3':
        a = int(input("Enter first number: "))
        b= int(input("Enter second number: "))
        print(a * b)
        print("MENU \n 1=ADD \n 2=SUBSTRACT \n 3=MULTIPLY \n 4=DIVIDE \n 5=QUIT ")
        ch = input('Enter your choice')
    if ch=='4':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a / b)
        print("MENU \n 1=ADD \n 2=SUBSTRACT \n 3=MULTIPLY \n 4=DIVIDE \n 5=QUIT ")
        ch = input('Enter your choice')
    if ch=='5':
        print("Quiting")
        break
    if ch>5:
        print("invalid vakue")


