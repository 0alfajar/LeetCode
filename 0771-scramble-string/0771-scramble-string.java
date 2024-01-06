public class Solution {
public boolean isScramble(String s1, String s2) {  
   int len = s1.length();  
   if (len != s2.length()) return false;  
   if (s1.equals(s2)) return true;  
   
   // a table of matches  
   // T[i][j][k] = true iff s2.substring(j,j+k+1) is a scambled string of s1.substring(i,i+k+1)  
   boolean[][][] scrambled = new boolean[len][len][len];  
   for (int i=0; i < len; ++i) {  
     for (int j=0; j < len; ++j) {  
       scrambled[i][j][0] = (s1.charAt(i) == s2.charAt(j));  
     }  
   }  
   
   // dynamically fill up the table  
   for (int k=1; k < len; ++k) { // k: length  
     for (int i=0; i < len - k; ++i) { // i: index in s1  
       for (int j=0; j < len - k; ++j) { // j: index in s2  
         scrambled[i][j][k] = false;  
         for (int p=0; p < k; ++p) { // p: split into [0..p] and [p+1..k]  
           if ((scrambled[i][j][p] && scrambled[i+p+1][j+p+1][k-p-1])  
               || (scrambled[i][j+k-p][p] && scrambled[i+p+1][j][k-p-1])) {  
             scrambled[i][j][k] = true;  
             break;  
           }  
         }  
       }  
     }  
   }  
   
   return scrambled[0][0][len-1];  
 }  

}