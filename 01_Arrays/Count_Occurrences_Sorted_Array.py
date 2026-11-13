# Count Occurrences in Sorted Array


class Solution:
    def countFreq(self, arr: List[int], target: int) -> int:
        def lower_bound(arr, target):
            low, high = 0, len(arr)

            while low < high:
                mid = (low + high) // 2

                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid

            return low

        def upper_bound(arr, target):
            low, high = 0, len(arr)

            while low < high:
                mid = (low + high) // 2

                if arr[mid] <= target:
                    low = mid + 1
                else:
                    high = mid

            return low

        return upper_bound(arr, target) - lower_bound(arr, target)
