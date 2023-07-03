def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    for i in range(m, (m+n)):
        nums1[i] = nums2[i-n]
    print (nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge (nums1, m, nums2, n)