class OldSolution(object):
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


class AlmostSolution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        p1 = 0
        p2 = 0
        idx = 0

        nums1_part = list(nums1[:m])

        while (p1 < m or p2 < n) and idx < m+n:
            if p1 < m and p2 < n:
                if nums2[p2] < nums1_part[p1]:
                    nums1[idx] = nums2[p2]
                    p2 += 1
                else:
                    nums1[idx] = nums1_part[p1]
                    p1 += 1

            elif p1 < m:
                nums1[idx] = nums1_part[p1]
                p1 += 1
            else:
                nums1[idx] = nums2[p2]
                p2 += 1

            idx += 1

        
class OptimalSolution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        p1 = m-1
        p2 = n-1
        idx = m+n-1

        while (p1 > -1 or p2 > -1) and idx > -1:
            # print(nums1)
            if p1 > -1 and p2 > -1:
                if nums2[p2] > nums1[p1]:
                    nums1[idx] = nums2[p2]
                    p2 -= 1
                else:
                    nums1[idx] = nums1[p1]
                    p1 -= 1

            elif p1 > -1:
                nums1[idx] = nums1[p1]
                p1 -= 1
            else:
                nums1[idx] = nums2[p2]
                p2 -= 1

            idx -= 1

        
'''
Revisited this problem and initially came up with the O(m+n) RT, O(m) space solution
"AlmostSolution". I then realized doing almost the exact same thing, but starting from
the ends of the arrays would mean using O(1) space, which lead me to "OptimalSolution", 
which has a runtime of O(m+n), and a space complexity of O(1)

Here's a similar discussion board solution

class Solution:
    def merge(self, nums1, m, nums2, n):
        midx = m - 1
        nidx = n - 1 
        right = m + n - 1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1

            right -= 1
'''
            
        
        