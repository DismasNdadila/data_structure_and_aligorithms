def int_to_roman(n):
    
    value_map = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    
    roman_numeral = ""

    
    for value, numeral in value_map:
       
        while n >= value:
           
            roman_numeral += numeral
            
            n -= value

    return roman_numeral

# Example usage
print(int_to_roman(2))     
print(int_to_roman(12))    
print(int_to_roman(27))    
print(int_to_roman(4))     
print(int_to_roman(9))     
print(int_to_roman(58))    
print(int_to_roman(1994))  
