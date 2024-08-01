class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """        
		
		# Convert length variables to be used as index
        lastI = len(nums1) - 1
        m = m - 1
        n = n - 1
		
		# Loop until one list is completed
        while m > -1 and n > -1:
            if nums1[m] > nums2[n]:
                nums1[lastI] = nums1[m]
                m -= 1
            else:
                nums1[lastI] = nums2[n]
                n -= 1
            lastI -= 1
        
		# Take care of leftover smaller integers on nums2. If there are leftover integers on nums1 instead, then the list is already sorted.
        while n > -1:
            nums1[lastI] = nums2[n]
            n -= 1
            lastI -= 1