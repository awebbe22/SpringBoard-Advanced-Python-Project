#Bubble Search
test0 = [3, 22, 14, 434, 501, 11, 9, 1230, 304, 123, 5412, 381923, 302, -3, 1]
 
test1 = [43, 12, 7, 9, 22, 1, 104]
 
test2 = [100, 0, 0, -20, 30, -5]
 
test3  = [28, 4, 17, 666, 1001, 52, 61, 30]


def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers)):
        for j in range(1, len(list_of_numbers)-i):
            if list_of_numbers[j-1] > list_of_numbers[j]: 
                temp = list_of_numbers[j-1]
                list_of_numbers[j-1] = list_of_numbers[j]
                list_of_numbers[j] = temp

    return list_of_numbers


print(test0)
print(bubble_sort(test0))

print(test1)
print(bubble_sort(test1))

print(test2)
print(bubble_sort(test2))

print(test3)
print(bubble_sort(test3))
