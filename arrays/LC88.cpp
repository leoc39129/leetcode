#include <vector>

class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        if(n == 0) {
            return;
        }
        if(m == 0) {
            nums1 = nums2;
            return;
        }
        int num1_idx = m - 1;
        int num2_idx = n - 1;
        

        for(int repl = m + n - 1; repl > -1; repl--) {
            if(num2_idx < 0) {
                nums1[repl] = nums1[num1_idx];
                num1_idx -= 1;
            } else if(num1_idx < 0) {
                nums1[repl] = nums2[num2_idx];
                num2_idx -= 1;
            } else if(nums2[num2_idx] > nums1[num1_idx]) {
                nums1[repl] = nums2[num2_idx];
                num2_idx -= 1;
            } else {
                nums1[repl] = nums1[num1_idx];
                num1_idx -= 1;
            }
        }

    }
};

/* 
RT: O(n + m)
Space: O(1)

This an optimal solution! However, while loops are more effective:

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int midx = m - 1;
        int nidx = n - 1;
        int right = m + n - 1;

        while (nidx >= 0) {
            if (midx >= 0 && nums1[midx] > nums2[nidx]) {
                nums1[right] = nums1[midx];
                midx--;
            } else {
                nums1[right] = nums2[nidx];
                nidx--;
            }
            right--;
        }        
    }
};
*/