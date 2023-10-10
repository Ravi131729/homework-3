def solution(lst, num):
    num_indices = {} #dictionary to store elements 
    for i, a in enumerate(lst):
        b = num - a  
        
        if b in num_indices:
            return a, b  
        
        num_indices[a] = i  
        
    return None  

#test case to find elements that add up to 13
numbers = [2,7,11,4]
print(solution(numbers, 13)) 

