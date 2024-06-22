def character_frequency(string):
  
    frequency = {}
    
    
    for char in string:
        
        char = char.lower()
        
       
        if char.isalpha():
            
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    
    return frequency
print(character_frequency("Hello, World!"))    
print(character_frequency("Python Programming"))  
print(character_frequency("12345!@#$%"))      
print(character_frequency("AAbbCC"))          
print(character_frequency("aAaAaA"))         
