/**
 * 30. Substring with Concatenation of All Words
 * 
 * Chang Li @ Sunnyvale
 * Jul. 27, 2016
 */
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> eligible_pos;
        if (words.empty()) return eligible_pos;
        const int word_len = words[0].size();
        const int word_num = words.size();
        unordered_map<string, int> word_dict;
        for (string word : words) {
            auto it = word_dict.find(word);
            if (it == word_dict.end()) {
                word_dict[word] = 1;
            } else {
                word_dict[word] ++;
            }
        }
        vector<unordered_map<string, int>> count_table(word_len, unordered_map<string, int>());
        vector<int> appeared(word_len, 0);
        for (int i=0; i+word_len<=s.size(); ++i) {
            auto& map = count_table[i%word_len];
            if (i - word_len*word_num >= 0) {
                string prev_word = s.substr(i-word_len*word_num, word_len);
                if (word_dict.find(prev_word) != word_dict.end()) {
                    map[prev_word] --;
                    if (map[prev_word] < word_dict[prev_word]) {
                        appeared[i%word_len] --;
                    }
                    if (map[prev_word] == 0) map.erase(prev_word);
                }
            }
            string curr_word = s.substr(i, word_len);
            if (word_dict.find(curr_word) != word_dict.end()) {
                auto it = map.find(curr_word);
                if (it != map.end()) {
                    it->second++;
                } else {
                    map[curr_word] = 1;
                }
                if (map[curr_word] <= word_dict[curr_word]) appeared[i%word_len] ++;
                if (appeared[i%word_len] == word_num) {
                    eligible_pos.push_back(i-word_len*(word_num-1));
                }
            }
        }
        return eligible_pos;
    }
};
