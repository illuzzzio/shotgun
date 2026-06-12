array = [1,1,2,4,5,6,7]

def contains_duplicates(array):
    for i in range(0,len(array)):
        for j in range(i+1, len(array)):
            if(array[i]==array[j]):
                return True
    return False 

print(contains_duplicates(array))


# more optimal solution 

def contain_duplicate_2(array):
    new_array = set(array)
    if(len(new_array)==len(array)):
        return False 
    else:
        return True 
    
print(contain_duplicate_2(array))
