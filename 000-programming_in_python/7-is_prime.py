def is_prime(number):
  
    if number <= 1:
        return False
    if number == 2:
        return True 
    if number % 2 == 0:
        return False  

    
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    
    return True
print(is_prime(2))    
print(is_prime(3))    
print(is_prime(4))    
print(is_prime(29))   
print(is_prime(100))  
print(is_prime(97))   
print(is_prime(1))    
print(is_prime(-7))   
