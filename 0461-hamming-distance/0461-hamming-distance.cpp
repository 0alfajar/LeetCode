class Solution {
public:
    int hammingDistance(int x, int y) {
        //return bitset<32>(x^y).count();
        int result = x ^ y;
        int count = 0;
        while (result > 0){
            count += result & 1;
            result >>= 1;
        }
        return count;
    }
};