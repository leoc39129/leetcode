class Solution:
    def checkPossibility(self, N):
        err = 0
        for i in range(1, len(N)):
            if N[i] < N[i-1]:
                if err or (i > 1 and i < len(N) - 1 and N[i-2] > N[i] and N[i+1] < N[i-1]):
                    return False
                err = 1
        return True

'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt_violations=0        
        for i in range(1, len(nums)):                       
            if nums[i]<nums[i-1]:
                if cnt_violations==1:
                    return False
                cnt_violations+=1
                if i>=2 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]                       
        return True
        # O(N) runtime, O(1) space
'''