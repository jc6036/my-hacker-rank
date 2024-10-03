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

        uint[] prefixArr = CreatePrefixSumArray(nums);

        if (prefixArr[prefixArr.Length-1] % p == 0)
        {
            return 0;
        }

        // Window pointers
        window arrWindow = new window();
        uint sum = 0; // Sum in a uint as inputs contain sums that will overflow an int

        while(arrWindow.end - arrWindow.start < nums.Length - 1)
        {
            sum = SumSubArrayFromPrefix(nums, prefixArr, arrWindow);
            {
                if(sum % p == 0)
                {
                    return (arrWindow.end - arrWindow.start) + 1;
                }
                else
                {
                    arrWindow = IncrementWindow(nums.Length, arrWindow);
                }
            }
        }

        return -1;        
    }

    public uint[] CreatePrefixSumArray(int[] nums)
    {
        uint sum = 0;
        uint[] prefixes = new uint[nums.Length];
        for(int i = 0; i < nums.Length; i++)
        {
            sum = sum + (uint)nums[i];
            prefixes[i] = sum;
        }

        return prefixes;
    }

    // Summing func that takes into account our window position
    public uint SumSubArrayFromPrefix(int[] nums, uint[] prefixes, window arrWindow) 
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
