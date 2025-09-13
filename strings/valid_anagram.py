def isAnagram(s, t):
  if len(s) != len(t):
        return False
  s_dict = {}

  for letter in s:
      if letter in s_dict:
          s_dict[letter] += 1 # if letter alr exists increment its count
      else:
          s_dict[letter] = 1
  
  for letter in t:
      if letter in s_dict:
          if s_dict[letter] == 1:
              del s_dict[letter]
          else:
              s_dict[letter] -= 1
      else:
          return False
  return True




isAnagram("anagram", "nagaram")

# {a: 2, c: 2}
# a n a g r a m
