# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# solution o(n)
def sortedSquares(self, nums):
    n = len(nums)
    left, right = 0, n - 1
    res = []
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            res.append(nums[left] ** 2)
            left += 1
        else:
            res.append(nums[right] ** 2)
            right -= 1
    return res[::-1]