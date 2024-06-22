def sum_even_numbers(my_list):
    
    sum_even = 0
    
    
    for number in my_list:
        
        if number % 2 == 0:
            
            sum_even += number
    
    return sum_even

print(sum_even_numbers([1, 2, 3, 4, 5, 6]))   
print(sum_even_numbers([10, 15, 20, 25, 30]))  
print(sum_even_numbers([7, 8, 9, 10, 11]))     
print(sum_even_numbers([1, 3, 5, 7, 9]))       
print(sum_even_numbers([]))             