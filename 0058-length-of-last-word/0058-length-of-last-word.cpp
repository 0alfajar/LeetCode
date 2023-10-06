class Solution {
public:
    int lengthOfLastWord(string s) {
        int count = 0;
        for(int i = s.length()-1; i >= 0; i--){
            while(int(s[i]==32)){
                i--;
            }
            while(int(s[i]!=32)){
                count++;
                i--;
                if(i < 0){
                    break;
                }
            }
            break;
        }
        return count;
    }
};