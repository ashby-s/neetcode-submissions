class Solution:
    def isValid(self, s: str) -> bool:
        
        p_stack = []
        start_p = ["{","[","("]
        end_p = ["}","]",")"]

        for char in s:
            if char in start_p:
                p_stack.append(char)
            elif char in end_p:
                if len(p_stack) > 0 and p_stack[-1] == start_p[end_p.index(char)]:
                    p_stack.pop()
                else:
                    return False
        
        if len(p_stack) > 0:
            return False
        return True

        