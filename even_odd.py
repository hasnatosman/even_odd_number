a = int(input("Input a number :"))
temp = 0
if a % 2 == 0:
    while temp <= a:
        print(temp)
        temp = temp + 2
else:
    temp = 1
    while temp <= a:
        print(temp)
        temp = temp + 2
