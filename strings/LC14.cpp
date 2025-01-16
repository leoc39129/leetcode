#include <string>
#include <vector>

class Solution {
public:
    std::string longestCommonPrefix(std::vector<std::string>& strs) {
        if(strs.size() == 1) {
            return strs[0];
        }
        
        std::string first = strs[0];
        std::string ret;
        int idx = 0;
        int count = 0;

        while(idx < first.size()) {
            // std::cout << idx << std::endl;
            // std::cout << first[idx] << std::endl;
            
            for(int i = 1; i < strs.size(); i++) {
                // std::cout << strs[i][idx] << std::endl;
                if(strs[i][idx] == first[idx]) {
                    count += 1;
                }
            }
            // std::cout << count << std::endl;
            if(count == strs.size() - 1) {
                ret += first[idx];
                idx += 1;
                count = 0;
            } else {
                break;
            }
        }
        return ret;
    }
};