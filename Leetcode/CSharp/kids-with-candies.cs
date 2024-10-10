public class Solution {
    public bool[] KidsWithCandies(int[] candies, int extraCandies) {
        int max = this.max(candies);
        bool[] result = new bool[candies.Length];
        for(int i = 0; i < candies.Length; i++)
        {
            if(candies[i] + extraCandies >= max)
            {
                result[i] = true;
            }
            else
            {
                result[i] = false;
            }
        }
        return result;
    }

    public int max(int[] candies)
    {
        int ret = 0;
        for(int i = 0; i < candies.Length; i++)
        {
            if(candies[i] > ret)
            {
                ret = candies[i];
            }
        }
        return ret;
    }
}

// Solution to Kids With the Greatest Number of Candies - beats 85%
