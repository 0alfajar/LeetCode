class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        size_t middle = nums.size() / 2;
        vector<int> firstHalf(nums.begin(), nums.begin() + middle);
        vector<int> secondHalf(nums.begin() + middle, nums.end());
        vector<int> shuffle;
        for(int i = 0; i < middle; i++){
            shuffle.push_back(firstHalf[i]);
            shuffle.push_back(secondHalf[i]);
        }
        return shuffle;
    }
};