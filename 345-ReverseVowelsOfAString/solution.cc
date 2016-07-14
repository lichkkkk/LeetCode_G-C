/**
 * 345. Reverse Vowels of a String
 * 
 * Chang Li @ Mountain view
 * Jul. 13, 2016
 */
class Solution {
public:
    string reverseVowels(string s) {
        int left = 0;
        int right = s.size()-1;
        while (left < right) {
            while (left < right && !isVowel(s[left])) left++;
            while (left < right && !isVowel(s[right])) right--;
            swap(s, left++, right--);
        }
        return s;
    }
    
    bool isVowel(char ch) {
        return ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'||
                ch=='A'||ch=='E'||ch=='I'||ch=='O'||ch=='U';
    }
    
    void swap(string& str, int ind1, int ind2) {
        char tmp = str[ind1];
        str[ind1] = str[ind2];
        str[ind2] = tmp;
    }
};
