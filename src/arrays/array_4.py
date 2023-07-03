def validMountainArray(arr: list[int]) -> bool:
    
    max_a = max(arr)
    top = False
    prev = arr[0]
    
    if len(arr) <= 2:
        return False
    
    if arr[-1] == max_a:
        return False
    
    for i in range(1, len(arr)):
        
        if top:
            if prev <= arr[i]:
                return False
        
        if not top:
            if prev >= arr[i]:
                return False
        
        prev = arr[i]
        
        if arr[i] == max_a:
            top = True
    
    return True
        
arr = [1,2,3,4,5,6,7,8,9]
print(validMountainArray(arr))