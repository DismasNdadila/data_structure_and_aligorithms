def get_smallest_integer(my_list):
   
    if not my_list:
        raise ValueError("The list is empty")
    
    
    smallest = my_list[0]
    
    for number in my_list:
        if number < smallest:
            smallest = number
print(get_smallest_integer([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  
print(get_smallest_integer([-1, -3, -5, -4, 0, 2, 3]))          
print(get_smallest_integer([42]))                       