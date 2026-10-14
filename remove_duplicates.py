class Solution:
    def remove_duplicate(self, arr):
        result = []
        for num in arr:
            if num not in result:
                result.append(num)
        return result


arr = [1, 2, 2, 3, 1, 4]
print(Solution().remove_duplicate(arr))