def calculate_slope(x1,x2,y1,y2):
    if x1==x2:
        return "The slope is undefined"
    slope = (y2 - y1) / (x2 - x1)
    return slope
x1=int(input("Enter x1:"))
x2=int(input("Enter x2:"))
y1=int(input("Enter y1:"))
y2=int(input("Enter y2:"))
print("Slope is:",calculate_slope(x1,x2,y1,y2))
