def groupAnagrams(strs):
    if len(strs) == 1:
        return [strs]

    d = {}
    for s in strs:
        s_sorted = sorted(s)
        s_str_sorted = "".join(s_sorted)
        if s_str_sorted not in d:
            d[s_str_sorted] = []
        d[s_str_sorted].append(s)
    
    anagrams = []
    for value in d.values():
      anagrams.append(value)
      
    return anagrams
    
    
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        