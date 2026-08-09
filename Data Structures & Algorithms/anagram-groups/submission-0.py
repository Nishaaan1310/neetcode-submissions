class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_map={}
        for string in strs:
            sorted_string= "".join(sorted(string))
            if sorted_string in string_map:
                string_map[sorted_string].append(string)
            else:
                string_map[sorted_string]=[string]
        output=[]

        for key in string_map:
            output.append(string_map[key])
        return output



