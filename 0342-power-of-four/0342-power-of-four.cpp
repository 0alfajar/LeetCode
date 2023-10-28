class Solution {
public:
    bool isPowerOfFour(int n) {
        if(n <= 0) return false;
        if(double(log(n)/log(4)) == int(log(n)/log(4))) return true;
        return false;
    }
};