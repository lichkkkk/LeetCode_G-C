class Solution {
    public String modifyString(String s) {
        char[] chs = s.toCharArray();
        char[] fillers = {'a', 'b', 'c'};
        for (int i=0; i<chs.length; i++) {
            if (chs[i] == '?') {
                for (char ch : fillers) {
                    if ((i > 0 && ch == chs[i-1]) || (i < chs.length - 1 && ch == chs[i+1])) {
                        continue;
                    }
                    chs[i] = ch;
                    break;
                }
            }
        }
        return String.valueOf(chs);
    }
}
