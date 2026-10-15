class Solution:
    def second_largest(self, arr):
        unique = sorted(set(arr))
        if len(unique) < 2:
            return -1
        return unique[-2]


arr = [10, 5, 8, 10, 3]
print(Solution().second_largest(arr))  
