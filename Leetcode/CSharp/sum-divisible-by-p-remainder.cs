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

        prefixes prefixContainer = CreatePrefixes(nums, p);
        int[] prefixArr = prefixContainer.prefixRemainders;
        long[] prefixSums = prefixContainer.prefixSums;

        String prefixRemOut = "";
        String prefixSumOut = "";
        for(int i = 0; i<prefixArr.Length;i++)
        {
            prefixRemOut = prefixRemOut + "," + prefixArr[i];
            prefixSumOut = prefixSumOut + "," + prefixSums[i];
        }
        /*Console.WriteLine(prefixRemOut);
        Console.WriteLine(prefixSumOut);*/

        if (prefixArr[prefixArr.Length - 1] == 0)
        {
            return 0;
        }

        // Window pointers
        window arrWindow = new window();

        while(arrWindow.end - arrWindow.start < nums.Length - 1)
        {
            if(prefixArr[prefixArr.Length - 1] == SubArrayRemainderFromPrefix(prefixArr, arrWindow, p) ||
               prefixArr[prefixArr.Length - 1] == SubArraySumFromPrefix(prefixSums, arrWindow, p))
            {
                return (arrWindow.end - arrWindow.start) + 1;
            }
            else
            {
                /*Console.WriteLine("Main Rem: {0}",prefixArr[prefixArr.Length-1]);
                Console.WriteLine("Point A: {0}, Point B: {1}",arrWindow.start,arrWindow.end);
                Console.WriteLine("Sub Remainder: {0}",SubArrayRemainderFromPrefix(prefixArr, arrWindow, p));
                Console.WriteLine("Sub Sum: {0}",SubArraySumFromPrefix(prefixSums, arrWindow, p));*/
                arrWindow = IncrementWindow(nums.Length, arrWindow);
            }
        }

        return -1;
    }

    public prefixes CreatePrefixes(int[] nums, int p)
    {
        prefixes ret = new prefixes();
        ret.prefixRemainders = new int[nums.Length];
        ret.prefixSums = new long[nums.Length];

        long sum = 0;
        for(int i = 0; i < nums.Length; i++)
        {
            sum = sum + (long)nums[i];
            ret.prefixSums[i] = sum;
            ret.prefixRemainders[i] = (int)(sum % (long)p);
        }

        return ret;
    }

    public int SubArrayRemainderFromPrefix(int[] prefixes, window arrWindow, int p)
    {
        if(arrWindow.start == 0)
        {
            return prefixes[arrWindow.end];
        }
        else
        {
            return (prefixes[arrWindow.end] + Math.Abs(p - prefixes[arrWindow.start - 1]));
        }
    }

    public long SubArraySumFromPrefix(long[] prefixes, window arrWindow, int p)
    {
        if(arrWindow.start == 0)
        {
            return prefixes[arrWindow.end];
        }
        else
        {
            return (prefixes[arrWindow.end] - prefixes[arrWindow.start - 1]);
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

    public struct prefixes
    {
        public int[] prefixRemainders;
        public long[] prefixSums;
    }
}
