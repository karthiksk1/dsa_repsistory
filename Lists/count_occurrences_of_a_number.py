class Solution:
    def count_occurrences(self, arr, target):
        count = 0
        for num in arr:
            if num == target:
                count += 1
        return count


arr = [2, 1, 2, 3, 2, 4]
print(Solution().count_occurrences(arr, 2))  
