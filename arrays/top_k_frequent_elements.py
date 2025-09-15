def topKFrequent(nums, k):
    d = {}
    for num in nums:
        if num not in d:
            d[num] = 1
        else:
            d[num] += 1
    d_sorted = sorted(d.items(), key=lambda item: item[1], reverse=True)
    
    result = []
    for i in range(k):
      result.append(d_sorted[i][0])
    return result



print(topKFrequent([1,3,1,2,2,1], 2))