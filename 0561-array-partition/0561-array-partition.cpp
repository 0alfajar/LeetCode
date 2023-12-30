class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size(), sum = 0, i = 0;

        while(i < n){
            sum += nums[i];
            i += 2;
        }
        return sum;
    }
};