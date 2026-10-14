class Solution:
    def left_rotate(self, arr):
        if not arr:
            return arr
        first = arr.pop(0)
        arr.append(first)
        return arr


arr = [1, 2, 3, 4, 5]
print(Solution().left_rotate(arr)) 