s = "pranjal"
t = "lajnarp"

def valid_anagram(s,t):
    return sorted(s)== sorted(t)

print(valid_anagram(s,t))   # O(nlogn)