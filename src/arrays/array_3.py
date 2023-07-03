def removeElement(nums: list[int], val: int) -> int:
    k = len(nums)
    
    while val in nums: 
        nums.remove(val)
        nums.append("_")
        k -= 1
        
    print(nums)
    return k
    
nums = [3,2,2,3]
val = 3
removeElement(nums, val)