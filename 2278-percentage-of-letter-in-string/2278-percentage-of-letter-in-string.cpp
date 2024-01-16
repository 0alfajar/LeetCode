class Solution {
public:
    int percentageLetter(string s, char letter) {
        int count = 0;
        for(int i = 0; i < s.size(); i++){
            if(s[i] == letter) count++;
        }
        return static_cast<int>((static_cast<double>(count) / s.size()) * 100);
    }
};