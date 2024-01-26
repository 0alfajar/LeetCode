class Solution {
public:
    int trailingZeroes(int n) {
        int factorial = 1;
        for(int i = 1; i <= n; i++){
            factorial *= i;
        }

        string s = to_string(factorial);
        int count = 0;
        for(int i = 0; i < s.size(); i++){
            if(s[i] == '0') count++;
        }
        return count;
    }
};