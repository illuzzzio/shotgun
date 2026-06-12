array = [1,2,4,5,6,7,8,5]
target = 10
def two_sum(array,target):
    for i in range (0,len(array)):
        for j in range(i+1,len(array)):
            if array[i]+array[j]==target:
                return [i,j]
print(two_sum(array,target))   # O(n^2) appracoach 


def best_two_sum_approach(array,target):
    hashmap = {}

    for i,v in enumerate(array):
        difference = target - v
        if difference in hashmap:
            return [hashmap[difference],i]
        hashmap[v] = i 

print(best_two_sum_approach(array,target))
     
