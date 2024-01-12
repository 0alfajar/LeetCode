class Solution {
public:
    int maximizeSum(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int curr = nums[nums.size() - 1];
        int sum = 0;
        for(int i = 1; i <= k; i++){
            sum += curr;
            curr++;
        }
        return sum;
    }
};