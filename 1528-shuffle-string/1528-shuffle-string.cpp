class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string shuffle = s;
        for(int i = 0; i < s.length(); i++){
            shuffle[indices[i]] = s[i];
        }
        return shuffle;
    }
};