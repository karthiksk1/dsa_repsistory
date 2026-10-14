class Solution:
    def smallest(self, arr):
        small = arr[0]
        for num in arr:
            if num < small:
                small = num
        return small


arr = [7, 3, 9, 1, 5]
print(Solution().smallest(arr)) 
