#Binary Search
def binary_search(list_of_numbers, query_item):
    index_first = 0
    index_last = len(list_of_numbers)-1
    found = False

    while index_first <= index_last and not found:         
        middle_index = (index_first+index_last)//2 
        if query_item == list_of_numbers[middle_index]:   
            found = True
            break
        else:
            if query_item < list_of_numbers[middle_index]:
	            index_last = middle_index - 1 
            else:
                index_first = middle_index + 1
    
    return found


test0 = [-3, 1, 3, 9, 11, 14, 22, 123, 302, 304, 434, 501, 1230, 5412, 381923]
print(binary_search(test0, 13))

test1 = [1, 7, 9, 12, 22, 43, 104]
print(binary_search(test1, 9))
 
test2 = [-20, -5, 0, 0, 30, 100]
print(binary_search(test2, 31))
 
test3 = [4, 17, 28, 30, 52, 61, 666, 1001]
print(binary_search(test3, 666))
