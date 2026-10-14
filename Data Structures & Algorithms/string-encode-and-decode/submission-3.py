class Solution:

    def encode(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return "None!None!None!"

        final_string = strs[0]
        strs.pop(0)
        for string in strs:
            final_string = final_string + "%%%" + string

        return final_string


    def decode(self, s: str) -> List[str]: 
        if s == "None!None!None!":
            print(s)
            arr = []
            return arr
        return s.split("%%%")
