s = "pranjal"
t = "lajnarp"

def valid_anagram(s,t):
    return sorted(s)== sorted(t)

print(valid_anagram(s,t))   # O(nlogn)


from collections import Counter 
def valid_anagram_2(s,t):

    if(len(s)!= len(t)):
        return False 
    s_dict = Counter(s)
    t_dict = Counter(t)
    return s_dict==t_dict


print(valid_anagram_2(s,t))


def best_valid_anagram(s,t):
    if len(s)!=len(t):
        return False 
    counter_dict = {}
    for ch in s:
        counter_dict[ch] = counter_dict.get(ch, 0) +1  # get syntx .get(key, defult value ) suppose in age doesnt exist in dict it will show none but if we use get it will show 0
    for ch in t:
        counter_dict[ch] = counter_dict.get(ch,0) -1

    for value in counter_dict.values():
        if value!= 0:
            return False 
    return True 

print(best_valid_anagram(s,t))

