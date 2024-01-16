class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int a = max(word1.size(), word2.size());
        string res = "";
        for(int i = 0; i < a; i++){
            if(i < word1.size()) res += word1[i];
            if(i < word2.size()) res += word2[i];
        }
        return res;
    }
};