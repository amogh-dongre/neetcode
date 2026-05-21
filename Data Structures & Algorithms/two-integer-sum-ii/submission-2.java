class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length -1;
        int res[] = new int[2];
        while(l<r){
            int curr_sum = numbers[l] + numbers[r];
            if(curr_sum < target)
               l++;
            else if (curr_sum > target)
              r--;
            else {
                res[0] = l+1;
                res[1] = r+1;
                break;
            }
        }
        return res;
    }
}
