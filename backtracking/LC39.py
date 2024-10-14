class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def recurse(candidates, target, cur):
            #print(cur)
            if target < 0:
                return None
            elif target == 0:
                ret.append(cur[1:])
            else:
                for num in candidates:
                    if cur and cur[-1] <= num:
                        arr = list(cur)
                        arr.append(num)
                        recurse(candidates, target - num, arr)
        
        candidates.sort()
        ret = []
        recurse(candidates, target, [0])
        return ret


'''
So I solved it! In O(n^n) RT, which is way worse than O(n!).

Here's a Python and Java discussion board solution. Notice how in Python we can't pass
res into the helper function, edit it, and then return it, but in Java you can. Low
level languages >>> ???

BASIC IDEA: Recursively call your helper function twice -- one including the current value
you're on, one excluding it and moving on. This will recursively build every combination
that's possible.

class Solution:
    def combinationSum(self, candidates, target):
            
        res = []

        def make_combination(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return
            
            if total > target or idx >= len(candidates):
                return
            
            comb.append(candidates[idx])
            make_combination(idx, comb, total + candidates[idx])
            comb.pop()
            make_combination(idx+1, comb, total)

            return res

        return make_combination(0, [], 0)


public List<List<Integer>> combinationSum(int[] nums, int target) {
    List<List<Integer>> list = new ArrayList<>();
    Arrays.sort(nums);
    backtrack(list, new ArrayList<>(), nums, target, 0);
    return list;
}

private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, int remain, int start){
    if(remain < 0) return;
    else if(remain == 0) list.add(new ArrayList<>(tempList));
    else{ 
        for(int i = start; i < nums.length; i++){
            tempList.add(nums[i]);
            backtrack(list, tempList, nums, remain - nums[i], i); // not i + 1 because we can reuse same elements
            tempList.remove(tempList.size() - 1);
        }
    }
}
'''