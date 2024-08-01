class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp = 0
        num = 0
        for x in range(0, len(nums1)):
            if n == 0:
                break
            if nums1[x] > nums2[-n]:
                num = nums1[x]
                nums1[x] = nums2[-n]
                n = n - 1
                # Need to shift all remaining vals one idx to the right
                for y in range(0, m):
                    temp = nums1[x+y+1]
                    nums1[x+y+1] = num
                    num = temp
            elif m == 0:
                nums1[x] = nums2[-n]
                n = n - 1
            else:
                m = m - 1
            
        
        