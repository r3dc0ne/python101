
my_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

for sub_list in my_list:
    print(sub_list)
    if sub_list[-1] == 10:
        print(sub_list[0])

print('#' * 10)

for sub_list_index in range(len(my_list)):
    print(my_list[sub_list_index])
    if my_list[sub_list_index][-1] == 10:
        print(my_list[sub_list_index][0])
