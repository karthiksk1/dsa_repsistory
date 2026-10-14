class Solution:
    def count_even(self, arr):
        count = 0
        for num in arr:
            if num % 2 == 0:
                count += 1
        return count


arr = [1, 2, 3, 4, 6, 7, 8]
print(Solution().count_even(arr))  