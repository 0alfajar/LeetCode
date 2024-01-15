class Solution {
public:
    int minimizedStringLength(string s) {
        int len = s.length();
        for(int i = 0; i < s.length() - 1; i++){
            for(int j = i + 1; j < s.length(); j++){
                if(s[i] == s[j]){
                    len--;
                    break;
                } 
            }
        }
        return len;
    }
};