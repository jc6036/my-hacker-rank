public class Solution {
    public string MergeAlternately(string word1, string word2) 
    {
        StringBuilder output = new StringBuilder();
        int word1Pointer = 0;
        int word2Pointer = 0;
        
        while(output.Length < word1.Length + word2.Length)
        {
            if(word1Pointer < word1.Length)
            {
                output.Append(word1[word1Pointer]);
                word1Pointer++;
            }

            if(word2Pointer < word2.Length)
            {
                output.Append(word2[word2Pointer]);
                word2Pointer++;
            }
        }

        return output.ToString();
    }
}

// Shortened version of the solution, with a slower runtime due to extra conditionals
