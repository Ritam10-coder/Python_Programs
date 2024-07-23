year=int(input("Enter the year:"))
if(year%400)or(year%100!=0)and(year%4==0):
    print("It is a Leap Year")
else:
    print("It is not a Leap Year")    