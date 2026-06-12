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
