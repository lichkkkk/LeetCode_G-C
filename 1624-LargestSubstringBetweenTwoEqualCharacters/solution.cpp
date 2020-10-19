class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        unordered_map<char, int> lmap;
        unordered_map<char, int> rmap;
        int li = 0;
        int ri = s.length() - 1;
        int res = -1;
        while (li <= ri && ri > res) {
            if (li != ri) {
                if (lmap.find(s[li]) == lmap.end()) lmap[s[li]] = li;
                if (rmap.find(s[ri]) == rmap.end()) rmap[s[ri]] = ri;
            }
            if (lmap.find(s[ri]) != lmap.end()) res = max(res, ri - lmap[s[ri]] - 1);
            if (rmap.find(s[li]) != rmap.end()) res = max(res, rmap[s[li]] - li - 1);
            li += 1;
            ri -= 1;
        }
        return res;
    }
};
