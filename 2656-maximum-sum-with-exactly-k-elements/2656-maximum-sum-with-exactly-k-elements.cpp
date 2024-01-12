class Solution {
public:
    int maximizeSum(vector<int>& nums, int k) {
        int m = *max_element(nums.begin(), nums.end());
        double two = 2;
        double k_over_2 = k / two; 
        return k * m + k_over_2 * (1+k) - k;
    }
};