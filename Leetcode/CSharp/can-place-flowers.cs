public class Solution {
    public bool CanPlaceFlowers(int[] flowerbed, int n) {
        int startingFlowers = this.CountFlowers(flowerbed);

        for(int i = 0; i < flowerbed.Length; i++) {
            if(flowerbed.Length == 1) {
                if(flowerbed[i] == 0) {
                    flowerbed[i] = 1;
                }
            }
            else {
                if(i == 0) {
                    if(flowerbed[i] == 0 && flowerbed[i+1] == 0) {
                        flowerbed[i] = 1;
                    }
                }
                else if(i == flowerbed.Length-1) {
                    if(flowerbed[i] == 0 && flowerbed[i-1] == 0)
                    {
                        flowerbed[i] = 1;
                    }
                }
                else
                {
                    if(flowerbed[i] == 0 && flowerbed[i-1] == 0 && flowerbed[i+1] == 0) {
                        flowerbed[i] = 1;
                    }
                }
            }
        }

        if(this.CountFlowers(flowerbed) - startingFlowers >= n) {
            return true;
        }
        else {
            return false;
        }
    }

    public int CountFlowers(int[] flowerbed)
    {
        int count = 0;
        for(int i = 0; i < flowerbed.Length; i++)
        {
            if(flowerbed[i] == 1)
            {
                count++;
            }
        }
        return count;
    }
}

// Solution for Can Place Flowers on leetcode. Beats 94%.
