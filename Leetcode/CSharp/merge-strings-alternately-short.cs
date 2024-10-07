public class Solution {
    unsafe public string MergeAlternately(string word1, string word2) 
    {
        StringBuilder output = new StringBuilder();
        int greaterLength = word1.Length > word2.Length ? word1.Length : word2.Length;
        int shorterLength = greaterLength == word1.Length ? word2.Length : word1.Length;
        int longerWord = greaterLength == word1.Length ? 1 : 2;

        for(int i = 0; i < shorterLength; i++)
        {
            output.Append(word1[i]);
            output.Append(word2[i]);
        }

        if(greaterLength != shorterLength)
        {
            if(longerWord == 1)
            {
                for(int i = shorterLength; i < greaterLength; i++)
                {
                    output.Append(word1[i]);
                }
            }
            else
            {
                for(int i = shorterLength; i < greaterLength; i++)
                {
                    output.Append(word2[i]);
                }
            }
        }

        return output.ToString();
    }
}
// Far better shortened version. Beats 90% on memory, 70% on runtime.
