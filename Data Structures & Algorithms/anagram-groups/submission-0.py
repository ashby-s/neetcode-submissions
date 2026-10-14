class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr_of_strs = []
        dict_of_dict = {}
        used = []

        for string in strs:
            string_dict = {}
            for char in string:
                if char in string_dict:
                    string_dict[char]+=1
                else:
                    string_dict[char] = 1

            dict_of_dict[string] = string_dict

        for string in dict_of_dict:
            if string not in used:
                tempstrs = []
                tempstrs.append(string)
                used.append(string)
                for string2 in dict_of_dict:
                    if string2 not in used and dict_of_dict[string] == dict_of_dict[string2]:
                        tempstrs.append(string2)
                        used.append(string2)
            
                arr_of_strs.append(tempstrs)
                    


        return arr_of_strs



