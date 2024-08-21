ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
length = len(ages)
if length % 2 == 0:
    median_age = (ages[length // 2 - 1] + ages[length // 2]) / 2
else:
    median_age = ages[length // 2]
average_age = sum(ages) / len(ages)    
print("Sorted ages:", ages)
print("Median age:", median_age)
print("Median age:", average_age)