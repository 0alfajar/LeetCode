class Solution {
public:
    int maximizeSum(vector<int>& nums, int k) {
        int curr = *max_element(nums.begin(), nums.end());
        int sum = 0;
        for(int i = 1; i <= k; i++){
            sum += curr;
            curr++;
        }
        return sum;
    }
};