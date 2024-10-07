public class Solution {
    public string MergeAlternately(string word1, string word2) 
    {
        StringBuilder output = new StringBuilder();
        int greaterLength = 0;
        int lesserLength = 0;
        bool longerWord = false;

        if(word1.Length == 0)
        {
            return word2;
        }
        else if(word2.Length == 0)
        {
            return word1;
        }

        if(word1.Length >= word2.Length)
        {
            greaterLength = word1.Length;
            lesserLength = word2.Length;
            longerWord = false;
        }
        else
        {
            greaterLength = word2.Length;
            lesserLength = word1.Length;
            longerWord = true;
        }

        if(greaterLength != lesserLength)
        {
            for(int i = 0; i < lesserLength; i++)
            {
                output.Append(word1[i]);
                output.Append(word2[i]);
            }
            if(longerWord == false)
            {
                for(int i = lesserLength; i < greaterLength; i++)
                {
                    output.Append(word1[i]);
                }
            }
            else
            {
                for(int i = lesserLength; i < greaterLength; i++)
                {
                    output.Append(word2[i]);
                }
            }
        }
        else
        {
            for(int i = 0; i < greaterLength; i++)
            {
                output.Append(word1[i]);
                output.Append(word2[i]);
            }
        }

        return output.ToString();
    }
}
