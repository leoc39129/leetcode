class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = [
            (1, "I"),
            (4, "IV"),
            (5, "V"),
            (9, "IX"),
            (10, "X"),
            (40, "XL"),
            (50, "L"),
            (90, "XC"),
            (100, "C"),
            (400, "CD"),
            (500, "D"),
            (900, "CM"),
            (1000, "M")
        ]
        idx = -1
        roman_arr = []
        while idx > -14:
            if num >= roman[idx][0]:
                roman_arr.append(roman[idx][1])
                num = num - roman[idx][0]
            else:
                idx -= 1
                

        return "".join(roman_arr)


'''
Good job recognizing that we can treat 900, 400, 90 ... as their own roman numerals

A better runtime comes from the following similar code. Strings are immutable, but only in that
you can't change specific characters of a string, you can always add to them (as in the line
where "result += symbol * count")

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Define Roman numeral mappings
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = ""
        
        # Iterate over the mapping
        for value, symbol in roman_map:
            # Determine how many times the symbol fits into the remaining number
            count = num // value
            if count > 0:
                # Append the symbol to the result as many times as it fits
                result += symbol * count
                # Reduce the number by the corresponding value
                num -= value * count
        
        return result

'''