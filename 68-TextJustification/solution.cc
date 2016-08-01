/**
 * 68. Text Justification
 * 
 * Chang Li @ Sunnyvale
 * Jul. 31, 2016
 */
class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> lines;
        vector<string> words_in_line;
        int len_of_line = 0;
        for (string word : words) {
            if (!words_in_line.empty() &&
                len_of_line+word.size()+1 > maxWidth) {
                lines.push_back(makeLine(words_in_line, maxWidth, 
                                         maxWidth-len_of_line, false));
                words_in_line.clear();
                len_of_line = 0;
            }
            words_in_line.push_back(word);
            len_of_line += word.size() + (words_in_line.size()==1 ? 0 : 1);
        }
        lines.push_back(makeLine(words_in_line, maxWidth,
                                 /* Won't be used */0, true));
        return lines;
    }
    
    string makeLine(const vector<string>& words, int length,
                    int additional_space_num, bool last_line) {
        if (words.size() == 1) {
            return words.front() + string(length-words.front().size(), ' ');
        }
        string line = "";
        for (int i=0; i<words.size()-1; ++i) {
            line += words[i];
            line += ' ';
            if (!last_line && additional_space_num > 0) {
                int gaps = words.size()-1-i;
                int spaces = additional_space_num / gaps;
                spaces += spaces*gaps < additional_space_num ? 1 : 0;
                line += string(spaces, ' ');
                additional_space_num -= spaces;
            }
        }
        line += words.back();
        if (last_line) line += string(length-line.size(), ' ');
        return line;
    }
};
