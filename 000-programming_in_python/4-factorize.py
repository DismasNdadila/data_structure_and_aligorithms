def factorize(number):
    # List to store the prime factors
    factors = []
    
    # Start dividing by 2
    divisor = 2
    
    # Continue factorizing until the number is greater than 1
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
        print(factorize(28))   
print(factorize(60))   
print(factorize(13))   
print(factorize(100))  
print(factorize(1))    