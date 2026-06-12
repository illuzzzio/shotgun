array = [1,2,4,5,6,7,7]

def contains_duplicates(array):
    for i in range(0,len(array)):
        for j in range(i+1, len(array)):
            if(array[i]==array[j]):
                return True
    return False 

print(contains_duplicates(array)) # O(n^2)


# more optimal solution 

def contain_duplicate_2(array):
    new_array = set(array)
    if(len(new_array)==len(array)):
        return False 
    else:
        return True 
    
print(contain_duplicate_2(array))  #O(1)


def contain_duplicate_3(array):
    array.sort()
    for i in range(0,len(array)-1):
        if(array[i]==array[i+1]):
            return True 
    return False 

print(contain_duplicate_3(array))  # if loop is from 0 to len(array) it means 0 to n-1 if lenght is 7 then 0 to 6 


