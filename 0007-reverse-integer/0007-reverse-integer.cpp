class Solution {
public:
    int reverse(long x) {
        bool negative = false;
        if (x < 0){
            negative = true;
            x *= -1;
        }
        long long reversed = 0;
        while(x > 0){
            reversed = (reversed * 10) + (x % 10);
            x /= 10;
        }
        if (reversed > INT_MAX){
            return 0;
        }

        if(negative){
            return -1 * reversed;
        } else {
            return reversed;
        }
    }
};