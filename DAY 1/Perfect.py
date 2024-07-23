
num = int(input("Enter the number:"))
Sum = 0
for i in range(1,num):
    if(num % i == 0):
        Sum = Sum + i
if (Sum == num):
    print("Number is a Perfect Number")
else:
    print("Number is not a Perfect Number")

