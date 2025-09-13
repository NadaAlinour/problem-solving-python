def pivotArray(nums, pivot):        
    if len(nums) == 1:
        return nums
    smaller = []
    larger = []
    pivots = []

    for num in nums:
        if num < pivot:
            smaller.append(num)
        elif num > pivot:
            larger.append(num)
        else: 
            pivots.append(num)    

    return smaller + pivots + larger 


print(pivotArray([9,12,5,10,14,3,10], 10))

# get index of pivot (10)
# -> 3
# [9,12,5,10,14,3,10]
# one element -> return nums
# two elements -> [num, pivot] -> num < pivot ? [num, pivot] : [pivot, num]
# [10, 10]
# three elements -> [2, 10, 5, 10, 3]
# smaller = [3]
# larger = [12]
# pivotArr = [10, 10]
# combine arrays = smaller + pivotArr + larger
