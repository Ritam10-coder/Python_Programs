fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'yogurt')
food_stuff_tp = fruits + vegetables + animal_products
print("food_stuff_tp:", food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print("food_stuff_lt:", food_stuff_lt)
middle_index = len(food_stuff_lt) // 2
middle_item = food_stuff_lt[middle_index]
print("Middle item(s):", middle_item)
