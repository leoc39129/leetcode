class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_wrds = set()
        if(len(words) == 0):
            return 0
        if(len(words) == 1):
            return 1
        ltrs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        translate = {}
        for i in range(len(ltrs)):
            translate[ltrs[i]] = morse[i]
        #print(translate["c"])
        for k in range(len(words)):
            morse_wrd_list = []
            for ltr in words[k]:
                morse_wrd_list.append(translate[ltr])
            morse_wrd = "".join(morse_wrd_list)
            morse_wrds.add(morse_wrd)
        print(morse_wrds)
        return len(morse_wrds)