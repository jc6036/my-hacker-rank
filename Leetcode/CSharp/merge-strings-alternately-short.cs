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

// Another version with some frankly ridiuclous and stupid optimizations thrown in

public class Solution {
    unsafe public string MergeAlternately(string word1, string word2) 
    {
        char* output = stackalloc char[word1.Length + word2.Length]; // Use char pointer instead of string builder for speed boost
        byte[] indices = [0,0,0,1]; // Slight speed boost by using an array instead of individual vars
        byte word1Length = (byte)word1.Length;
        byte word2Length = (byte)word2.Length;
        /*int bufIndex = 0;
        int greaterLength = 0;
        int shorterLength = 0;
        int longerWord = 1;*/

        if(word1Length >= word2Length)
        {
            indices[1] = word1Length;
            indices[2] = word2Length;
        }
        else
        {
            indices[1] = word2Length;
            indices[2] = word1Length;
            indices[3] = 2;
        }

        for(int i = 0; i < indices[2]; i++)
        {
            output[indices[0]] = word1[i];
            indices[0]++;
            output[indices[0]] = word2[i];
            indices[0]++;
        }

        if(indices[1] != indices[2])
        {
            if(indices[3] == 1)
            {
                for(int i = indices[2]; i < indices[1]; i++)
                {
                    output[indices[0]] = word1[i];
                    indices[0]++;
                }
            }
            else
            {
                for(int i = indices[2]; i < indices[1]; i++)
                {
                    output[indices[0]] = word2[i];
                    indices[0]++;
                }
            }
        }

        return new String(output, 0, word1.Length + word2.Length);
    }
}

// My final optimization that beat 90% runtime
public class Solution {
    unsafe public string MergeAlternately(string word1, string word2) 
    {
        StringBuilder output = new StringBuilder();
        byte[] indices = [0,0,0,1]; // Slight speed boost by using an array instead of individual vars
        byte word1Length = (byte)word1.Length;
        byte word2Length = (byte)word2.Length;
        /*int bufIndex = 0;
        int greaterLength = 0;
        int shorterLength = 0;
        int longerWord = 1;*/

        if(word1Length >= word2Length)
        {
            indices[1] = word1Length;
            indices[2] = word2Length;
        }
        else
        {
            indices[1] = word2Length;
            indices[2] = word1Length;
            indices[3] = 2;
        }

        for(int i = 0; i < indices[2]; i++)
        {
            output.Append(word1[i]);
            output.Append(word2[i]);
        }

        if(indices[1] != indices[2])
        {
            if(indices[3] == 1)
            {
                for(int i = indices[2]; i < indices[1]; i++)
                {
                    output.Append(word1[i]);
                }
            }
            else
            {
                for(int i = indices[2]; i < indices[1]; i++)
                {
                    output.Append(word2[i]);
                }
            }
        }

        return output.ToString();
    }
}


// Final optimization, beats 97%
public class Solution {
    unsafe public string MergeAlternately(string word1, string word2) 
    {
        StringBuilder output = new StringBuilder();
        byte minLength = (byte)Math.Min(word1.Length, word2.Length);
        byte greaterWord = (byte)((byte)word1.Length > (byte)word2.Length ? 1 : 2);
        
        for(byte i = 0; i < minLength; i++)
        {
            output.Append(word1[i]);
            output.Append(word2[i]);
        }

        if(greaterWord == 1)
        {
            return output.Append(word1.Substring(minLength)).ToString();
        }
        else
        {
            return output.Append(word2.Substring(minLength)).ToString();
        }
    }
}
