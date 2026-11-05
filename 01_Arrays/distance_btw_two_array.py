class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0

        for x in arr1:
            left, right = 0, len(arr2) - 1
            valid = True

            while left <= right:
                mid = (left + right) // 2

                if abs(x - arr2[mid]) <= d:
                    valid = False
                    break
                elif arr2[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1

            if valid:
                count += 1

        return count
