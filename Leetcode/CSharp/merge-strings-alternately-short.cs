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


// This solution uses a pointer to create the string rather than stringbuilder, but stringbuilder is actually faster
public class Solution {
    unsafe public string MergeAlternately(string word1, string word2) 
    {
        int totalLength = word1.Length + word2.Length;
        char* output = stackalloc char[totalLength];
        int bufIndex = 0;

        int greaterLength = word1.Length > word2.Length ? word1.Length : word2.Length;
        int shorterLength = greaterLength == word1.Length ? word2.Length : word1.Length;
        int longerWord = greaterLength == word1.Length ? 1 : 2;

        for(int i = 0; i < shorterLength; i++)
        {
            output[bufIndex] = word1[i];
            bufIndex++;
            output[bufIndex] = word2[i];
            bufIndex++;
        }

        if(greaterLength != shorterLength)
        {
            if(longerWord == 1)
            {
                for(int i = shorterLength; i < greaterLength; i++)
                {
                    output[bufIndex] = word1[i];
                    bufIndex++;
                }
            }
            else
            {
                for(int i = shorterLength; i < greaterLength; i++)
                {
                    output[bufIndex] = word2[i];
                    bufIndex++;
                }
            }
        }

        return new String(output, 0, totalLength);
    }
}
