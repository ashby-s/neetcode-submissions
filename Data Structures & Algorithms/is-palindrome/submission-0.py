class Solution:
    def isPalindrome(self, s: str) -> bool:
        index1 = 0
        index2 = len(s)-1

        while index1 < index2:
            while not(s[index1].isalnum()):
                index1+=1

            while not(s[index2].isalnum()):
                index2-=1

            if s[index1].lower() != s[index2].lower():
                return False;
            index1+=1
            index2-=1
        
        return True