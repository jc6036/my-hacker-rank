public class Solution {
    public int MinSubarray(int[] nums, int p)
    {
        // Sliding window algorithm
        // Check if nums % p == 0
        // If not, sliding window at 0, width = 1
        // Check if sum(nums minus window elements) % p == 0
        // If not, increment sliding window to 1:1 and so on until end
        // Once we hit the end, sliding window length++, start over at 0:1
        // Repeat until we've checked all contigious subarray answers
        // If we never find a valid answer once the window len == array len, return -1
        // Update: this is also a prefix problem, not just sliding windows. 
        // Should've known, find longest/smallest sub-x of x is almost always prefix
        // Problem included hints about remainders, including mapping a prefix of all sum remainders
        // For any given sub-array, removing it will subtract the sub-array's remainder from the main array's
        // Therefore instead of performing %, you can instead do a single subtract operation to check if you 
        // will have a divisible sum by removing the sub array. Answer is simple there, % is more expensive
        // than a subtract and compare, should make it faster in theory.

        int[] prefixArr = CreatePrefixRemainderArray(nums, p);

        if (prefixArr[prefixArr.Length - 1] == 0)
        {
            return 0;
        }

        // Window pointers
        window arrWindow = new window();

        while(arrWindow.end - arrWindow.start < nums.Length - 1)
        {
            if(MainArrayRemainderFromPrefix(prefixArr, arrWindow) == SubArrayRemainderFromPrefix(prefixArr, arrWindow))
            {
                return (arrWindow.end - arrWindow.start) + 1;
            }
            else
            {
                arrWindow = IncrementWindow(nums.Length, arrWindow);
            }
        }

        return -1;
    }

    public int[] CreatePrefixRemainderArray(int[] nums, int p)
    {
        long sum = 0;
        int[] prefixes = new int[nums.Length];
        for(int i = 0; i < nums.Length; i++)
        {
            sum = sum + (long)nums[i];
            prefixes[i] = (int)(sum % (long)p);
        }

        return prefixes;
    }

    public int SubArrayRemainderFromPrefix(int[] prefixes, window arrWindow)
    {
        if(arrWindow.start == 0)
        {
            return prefixes[arrWindow.end];
        }
        else
        {
            return prefixes[arrWindow.end] - prefixes[arrWindow.start - 1];
        }
    }

    public long MainArrayRemainderFromPrefix(int[] prefixes, window arrWindow) 
    {
        if(arrWindow.start == 0)
        {
            return prefixes[prefixes.Length-1] - prefixes[arrWindow.end];
        }
        else if (arrWindow.end == prefixes.Length - 1)
        {
            return prefixes[arrWindow.start - 1];
        }
        else
        {
            return prefixes[arrWindow.start - 1] + (prefixes[prefixes.Length-1] - prefixes[arrWindow.end]);            
        }
    }

    public window IncrementWindow(int arrLength, window arrWindow)
    {
        int length = arrWindow.end - arrWindow.start;

        // At the end of the array, go back to start and grow window
        if(arrWindow.end == arrLength - 1)
        {
            length++;
            arrWindow.start = 0;
            arrWindow.end = 0 + length;

            return arrWindow;
        }
        // Otherwise increment both up one to slide the window
        else
        {
            arrWindow.start++;
            arrWindow.end++;

            return arrWindow;
        }
    }

    public struct window
    {
        public window(int in_start = 0, int in_end = 0)
        {
            start = in_start;
            end = in_end;
        }

        public int start;
        public int end;
    }
}
