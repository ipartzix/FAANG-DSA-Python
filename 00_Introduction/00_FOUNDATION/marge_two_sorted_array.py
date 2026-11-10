left = [1,2,3,4]
right = [1,1,3,4,5,6,7]

def margeArr (left,right):
    result = []
    i , j = 0 ,0
    n, m = len(left),len(right)
    while i <n and j <m :
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i < n:
        while i <n :
            result.append(left[i])
            i+=1
    if j< m:
        while j<m:
            result.append(right[j])
            j+=1
    print(result)
margeArr(left,right)

# leetcode: 88. Merge Sorted Array  https://leetcode.com/problems/merge-sorted-array/description/?envType=problem-list-v2&envId=array

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
