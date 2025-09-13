# O(n) solution
def containsDuplicate(nums):
    dict = {}
    for idx, num in enumerate(nums):
        if num in dict:
            return True
        dict[num] = idx
    return False
  
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
  
  # think of a faster solution!
  
  