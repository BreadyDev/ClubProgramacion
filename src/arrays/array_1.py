
def findMaxConsecutiveOnes(nums: list[int]) -> int:
    consecutive = 0
    max_con = 0
    
    for num in nums:
        
        if num == 1:
            consecutive += 1
        else:
            consecutive = 0 
        
        max_con = max(consecutive, max_con)
        
    print(max_con)

            
nums = [1,0,1,1,0,1]
findMaxConsecutiveOnes(nums)