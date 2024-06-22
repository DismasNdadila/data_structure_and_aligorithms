def find_first_occurrence(my_list, num):
    
    for index, value in enumerate(my_list):
        if value == num:
            return index
    
    return -1
print(find_first_occurrence([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 5))  
print(find_first_occurrence([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 7))  
print(find_first_occurrence([1, 2, 3, 4, 5], 3))                    
print(find_first_occurrence([10, 20, 30, 40, 50], 10))              
print(find_first_occurrence([10, 20, 30, 40, 50], 60)) 