class Solution:
    def move_zero(self, arr):
        non_zero = []
        zero = []
        for num in arr:
            if num == 0:
                zero.append(num)
            else:
                non_zero.append(num)
        return non_zero + zero


arr = [0, 1, 0, 3, 12]
print(Solution().move_zero(arr))
