class Solution:
    def reverseWords(self, s: str) -> str:
        start = -1
        end = -1
        ret = ""
        s = s.strip()
        for i in range(len(s)-1, -1, -1):
            if end == -1 and s[i] != " ":
                end = i
            
            if start == -1 and end != -1 and s[i] == " ":
                start = i + 1

            if start == -1 and end != -1 and i == 0:
                start = 0
            
            if start != -1 and end != -1:
                ret = ret + s[start:end+1]
                if start > 0:
                    ret = ret + " "
                start = -1
                end = -1
            
        return ret
# Solution to leetcode Reverse Words in a String, beats 98%
