class Solution:

    def encode(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return chr(257)

        final_string = strs[0]
        strs.pop(0)
        for string in strs:
            final_string = final_string + chr(256) + string

        return final_string

    def decode(self, s: str) -> List[str]:
        if s == chr(257):
            return []

        return s.split(chr(256))