/**
 * 65. Valid Number
 * Tag: String, Compiler, Parser
 * Chang Li at UC San Diego
 * Feb. 19, 2016
 */

bool isSimpleNumber(char *s, int len, bool isInteger);

bool isNumber(char* s) {
    if (!s) return false;
    
    // Get the length
    int len = 0;
    for (len=0; s[len] != '\0'; len++);
    
    // Remove spaces in two sides
    while (s[0] == ' ') {s++; len--;}
    while (s[len-1] == ' ' && len >= 1) len--;
    if (len == 0) return false;
    
    // Check if include exp
    int expPos;
    for (expPos=0; expPos<len && s[expPos] != 'e'; expPos++);
    
    // Check if is valid number
    if (expPos < len) {
        return isSimpleNumber(s, expPos, false) && isSimpleNumber(s+expPos+1, len-expPos-1, true);
    } else {
        return isSimpleNumber(s, len, false);
    }
}

bool isSimpleNumber(char* s, int len, bool isInteger) {
    if (len<=0 || !s) return false;
    
    // Jump over the -/+
    if (s[0] == '-' || s[0] == '+') {s++; len--;}
    
    bool decimalAppeared = isInteger;
    bool isEmpty = true;
    
    // Scan
    for (int i=0; i<len; i++) {
        if (s[i] >= '0' && s[i] <= '9') {
            isEmpty = false;
            continue;
        } else if (s[i] == '.' && !decimalAppeared) {
            decimalAppeared = true;
        } else {
            return false;
        }
    }
    
    return !isEmpty;
}