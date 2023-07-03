def sortArrayByParity(nums: list[int]) -> list[int]:

    left = 0  # Pointer for even numbers
    right = len(nums) - 1  # Pointer for odd numbers

    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 != 0:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    print(nums)
    
nums = [0,1]
sortArrayByParity(nums)