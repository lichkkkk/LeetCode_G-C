/*
 * Scan from head to tail. Maintain the last met string.
 *
 * Running Time: O(n)
 * Chang Li at UC San Diego
 * Dec. 15, 2015
 */

class Solution {
public:
    int shortestDistance(vector<string>& words, string word1, string word2) {
        
        bool first = true;
        int res = words.size();
		// var to store the last string & pos        
        string last_string;
        int last_pos;
        // scan from head to end
        for(int i=0; i<words.size(); i++) {
            if(words[i] == word1 || words[i] == word2) {
                if(first) {
                    last_string = words[i];
                    last_pos = i;
                    first = false;
				// If meet different, update min distance and swap
                }else if(words[i] != last_string) {
                    if(i - last_pos < res) {
                        res = i - last_pos;
                        last_pos = i;
                        last_string = words[i];
                    }else {
                        last_pos = i;
                        last_string = words[i];
                    }
                }else {
                    last_pos = i;
                }
            }
        }
        return res;
    }
};
