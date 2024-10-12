public class Solution {
    public string ReverseVowels(string s) {
        char[] vowels = ['a','e','i','o','u'];
        List<int> vowelPositions = new List<int>();
        char[] cs = s.ToCharArray();

        for(int i = 0; i < s.Length; i++) {
            if(this.Contains(char.ToLower(s[i]), vowels)) {
                vowelPositions.Add(i);
            }
        }
        
        for(int front = 0, back = vowelPositions.Count - 1; front < vowelPositions.Count / 2; front++, back--)
        {
            char tmp = cs[vowelPositions[front]];
            cs[vowelPositions[front]] = cs[vowelPositions[back]];
            cs[vowelPositions[back]] = tmp;
        }

        return new String(cs);
    }

    public bool Contains(char input, char[] vowels) {
        for(int i = 0; i < vowels.Length; i++) {
            if(input == vowels[i]) {
                return true;
            }
        }

        return false;
    }
}

// Solution for leetcode Reverse Vowels of a String - beats 60%
