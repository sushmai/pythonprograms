class Solution(object):
    def uniqueMorseRepresentations(self, words):
        #word = input("enter a word")
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                 for word in words}

        return len(seen)

    
    
        

