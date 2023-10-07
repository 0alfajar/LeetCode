class Solution {
public:
    int arrangeCoins(int n) {
        int k = 0;
        while(n > 0){
            k++;
            n -= k;
        }
        if(n == 0) return k;
        else return k -1;
    }
};

