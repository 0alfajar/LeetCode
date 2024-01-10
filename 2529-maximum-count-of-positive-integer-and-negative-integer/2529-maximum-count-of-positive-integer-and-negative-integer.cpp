class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int negative = 0, positive = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] < 0) negative++;
            else if(nums[i] > 0) positive++;
        }
        return max(negative, positive);
    }
};