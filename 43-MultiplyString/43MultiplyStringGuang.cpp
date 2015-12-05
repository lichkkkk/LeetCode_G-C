class Solution {
public:
    
    
// s is gurranted to be long enough, appended with 0's when necessary
string multiplyANum(string &s, int num, int st, int len){
        string res(len, '0');
        if(num == 0) return res;

        int carry = 0;
        for(int i = 0; i < s.size(); i++){
                int tmp = carry + (s[i]-'0')*num;
                res[i+st] = tmp%10 + '0';
                carry = tmp/10;
        }
        res[s.size() + st] = '0' + carry;
        return res;

}

string addTwoString(string s1, string s2){
        string res(s1.size(), '0');
        int carry = 0;
        for(int i = 0; i < s1.size(); ++i){
                int tmp = s1[i]-'0' + s2[i]-'0' + carry;
                res[i] = tmp%10 + '0';
                carry = tmp/10;
        }
        return res;
}
string multiplyTwoString(string str1, string str2){
        int len1 = str1.size(), len2 = str2.size();
        int len = len1 + len2;
        string res(len, '0');
        for(int i = 0; i < len2; i++){
                string s1 = multiplyANum(str1, str2[i]-'0', i, len);
                res = addTwoString(res, s1);
        }

        return res;

}
string multiply(string num1, string num2){
        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());
        string num = multiplyTwoString(num1, num2);
        int st = num.size()-1;
        while(st >0 && num[st] == '0') st--;
        string res(num.begin(), num.begin()+st+1);
        reverse(res.begin(), res.end());
        return res;
}


};
