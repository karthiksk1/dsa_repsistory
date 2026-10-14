class Solution:
    def sum_array(self, arr):
        total = 0
        for num in arr:
            total += num
        return total


arr = [1, 2, 3, 4]
print(Solution().sum_array(arr)) 