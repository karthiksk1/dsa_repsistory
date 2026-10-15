class Solution:
    def isSorted(self, arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True


arr = [1, 2, 2, 4, 5]
result = Solution().isSorted(arr)
print("Is array sorted:", result)
