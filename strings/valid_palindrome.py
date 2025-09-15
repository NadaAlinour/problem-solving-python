def isPalindrome(s):
  if s == "":
      return True
  s_filtered = "".join([c for c in s if c.isalnum()]).lower()
  s_list = list(s_filtered)
  
  low = 0
  high = len(s_list) - 1
  while low <= high:
    if s_list[low] != s_list[high]:
      return False
    low += 1
    high -= 1
  return True
      
    
print(isPalindrome("0P"))