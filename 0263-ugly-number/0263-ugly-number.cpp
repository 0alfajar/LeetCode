class Solution {
public:
    bool isUgly(int n) {
        if(n == 1) return true;
        else if (n % 2 == 0 && n % 3 == 0 && n % 5 == 0) return true;
        else if (n % 2 == 0 && n % 3 == 0) return true;
        else if (n % 2 == 0 && n % 5 == 0) return true;
        else if (n % 3 == 0 && n % 5 == 0) return true;
        else return false;
    }
};