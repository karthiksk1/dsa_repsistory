class Solution:
    def search(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1


arr = [10, 20, 30, 40]
target = 30
print(Solution().search(arr, target))
