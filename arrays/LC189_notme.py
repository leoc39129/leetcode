class Solution:
    def rotate(self, nums, k):
        k %= len(nums)
        self.reverseArray(0, len(nums) - 1, nums)
        self.reverseArray(0, k - 1, nums)
        self.reverseArray(k, len(nums) - 1, nums)

    def reverseArray(self, left, right, array):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1