def two_indices(nums, target):
    
    num_to_index = {}
    
   
    for index, num in enumerate(nums):
        
        complement = target - num
        
        
        if complement in num_to_index:
           
            return [num_to_index[complement], index]
        
        
        num_to_index[num] = index
#example ;

nums = [2, 7, 11, 15]
target = 9
print(two_indices(nums, target))  
print(two_indices([2, 7, 11, 15], 9))  
print(two_indices([3, 2, 4], 6))       
print(two_indices([3, 3], 6))          
print(two_indices([1, 2, 3, 4], 7))    
print(two_indices([10, 5, 2, 7], 9))   
