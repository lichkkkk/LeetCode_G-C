/**
 * 186. Reverse Words in a String II
 * Tag: String
 * Chang Li at UC San Diego
 * Feb. 11, 2016
 */

void reverseWords(char *s) {
    int lastSpace = 0;
    int currPos = 0;
    char ch;
    do {
        ch = *(s + currPos);
        if (ch == ' ' || ch == '\0') {
            reverseSingleWord(s, lastSpace, currPos - 1);
            lastSpace = currPos + 1;
        }
        currPos ++;
    } while (ch != '\0');
    reverseSingleWord(s, 0, currPos-2);
}

void reverseSingleWord(char *s, int start, int end) {
    if(!s || start < 0 || start >= end) return;
    
    while (start < end) {
        char tmp = *(s + start);
        *(s + start) = *(s + end);
        *(s + end) = tmp;
        start ++;
        end --;
    }
}
