class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n < 1) return false;
        for(int i = 0; i <= cbrt(n); i++){
            if(pow(3, i) == n) return true;
            if(pow(3, i) > n) return false;
        }
        return false;
    }
};