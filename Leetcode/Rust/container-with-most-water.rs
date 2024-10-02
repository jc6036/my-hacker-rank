impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        // 1. Define 2 'pointers' at 0 and len(height) - 1 (y, z)
        // 2. Calculate area of current selection via Length = y - z. Area = length * the smaller of y or z
        // 3. Save area to holding var if > than current answer
        // 4. Of the smaller of the two options, increment/deincrement as needed until y - z == 1
        // 5. Return answer

        let mut y: usize = 0;
        let mut z: usize = height.len() - 1;

        let mut answer: usize = 0;
        while y < z {
            if(if(height[z] >= height[y]) {(z - y) * height[y] as usize} else {(z - y) * height[z] as usize}) > answer {
                answer = if(height[z] >= height[y]) {(z - y) * height[y] as usize} else {(z - y) * height[z] as usize}
            }

            if height[y] <= height[z] {
                y += 1;
            }
            else {
                z = z - 1;
            }
        }

        return answer as i32;
    }
}

// "Container With Most Water" problem on leetcode
