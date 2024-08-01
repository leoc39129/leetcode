class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        my_dict = {}
        min_count = 1001
        res = []
        for j in range(len(list2)):
            my_dict[list2[j]] = j
        for i in range(len(list1)):
            if list1[i] in my_dict:
                if min_count == 1001:
                    res.append(list1[i])
                    min_count = i + my_dict[list1[i]]
                elif i + my_dict[list1[i]] < min_count:
                    res = [list1[i]]
                elif i + my_dict[list1[i]] == min_count:
                    res.append(list1[i])
        return res
            
