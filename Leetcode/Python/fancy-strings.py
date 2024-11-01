class Solution:
    def makeFancyString(self, s: str) -> str:
        rebuilt_string = ""
        count = 1
        current = ''

        for letter in s:
            if letter != current:
                current = letter
                count = 1
            else:
                count = count + 1
            
            if count < 3:
                rebuilt_string = rebuilt_string + letter
        
        return rebuilt_string

# Solution for leetcode Delete Characters to Make Fancy String, beats 90%
