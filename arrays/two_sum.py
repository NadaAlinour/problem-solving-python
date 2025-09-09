# find the indices of a pair of integers within the array
# (without using the same element more than once) that add up to a target integer


# [2, 7, 11, 15] -> [0, 1]
# brute force method
def two_sum_brute_force(nums, target):
  for idx, num in enumerate(nums):
    for i in range(1, len(nums)):
      if nums[i] + num == target:
        return [idx, i]
    return None

# binary search method
# takes sorted array
def binary_search(needle, haystack):
  min = 0
  max = len(haystack) - 1
  
  while (min <= max):
    mid = (max + min) // 2
    
    if haystack[mid][0] == needle:
      return haystack[mid]
    if haystack[mid][0] > needle:
      max = mid - 1
    if haystack[mid][0] < needle:
      min = mid + 1
    
  return (-1, -1)


def two_sum_with_binary_search(nums, target):
  hash_nums = {(num, idx) for idx, num in enumerate(nums)}
  sorted_hash_nums = sorted(hash_nums, key=lambda x: x[0])
  
  for idx, num in enumerate(nums):
    diff = target - num
    req_idx = binary_search(diff, sorted_hash_nums)
    if req_idx[1] != -1:
      return [idx, req_idx[1]]




# two-pointers method
def two_sum_two_pointers(nums, target):
  lo = 0
  hi = len(nums) - 1
  
  nums_sorted = sorted(nums)
  
  while lo <= hi:
    sum = nums_sorted[lo] + nums_sorted[hi]
    if  sum == target:
      return [lo, hi]
    
    elif sum < target:
      lo = lo + 1
      
    else: hi = hi - 1
    
  return -1
  



# hash table method
def two_sum_hash(nums, target):
  # create hash table with key as num and value as index
  hash_nums = {num: idx for idx, num in enumerate(nums)}
  for idx, num in enumerate(nums):
    diff = target - num
    if diff in hash_nums and idx != hash_nums[diff]:

      return [idx, hash_nums[diff]]



nums = [2, 7, 11, 15]
target = 9

# print(two_sum_brute_force(nums, target))
# print(two_sum_hash(nums, target))
# print(two_sum_with_binary_search(nums, target))
# print(two_sum_two_pointers(nums, target))