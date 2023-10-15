class Solution {
public:
    string intToRoman(int num) {
        string satuan[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        string puluhan[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        string ratusan[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        string ribuan[] = {"", "M", "MM", "MMM"};

        return ribuan[num/1000] + ratusan[(num%1000)/100] + puluhan[(num%100)/10] + satuan[num%10];
    }
};