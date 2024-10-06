public class Solution {
    public int MinSubarray(int[] nums, int p)
    {
        int[] prefixArr = CreatePrefixes(nums, p);

        if (prefixArr[prefixArr.Length - 1] == 0)
        {
            return 0;
        }

        // Window pointers
        window arrWindow = new window();

        while(arrWindow.end - arrWindow.start < nums.Length - 1)
        {
            int rem = CalculateMainArrayRemainder(prefixArr, arrWindow);
            if(rem == 0 || rem == p)
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

    public int[] CreatePrefixes(int[] nums, int p)
    {
        int[] ret = new int[nums.Length];
        long sum = 0;
        for(int i = 0; i < nums.Length; i++)
        {
            sum = sum + (long)nums[i];
            ret[i] = (int)(sum % (long)p);
        }

        return ret;
    }

    public int CalculateMainArrayRemainder(int[] prefixArr, window arrWindow)
    {
        if(arrWindow.start == 0)
        {
            return Math.Abs(prefixArr[prefixArr.Length-1] - prefixArr[arrWindow.end]);
        }
        else
        {
            return Math.Abs((prefixArr[prefixArr.Length-1] - prefixArr[arrWindow.end]) + prefixArr[arrWindow.start-1]);
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
