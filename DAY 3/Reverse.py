def reverse_list(lst):
    r_list = []
    for i in range(len(lst)-1, -1, -1):
        r_list.append(lst[i])
    return r_list
array = [1, 2, 3, 4, 5]
r_list = reverse_list(array)
print(r_list)
