/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    // Assume word.length > 0, only [a-zA-Z]
    return word == word.toUpperCase() 
        || word.substring(1) == word.substring(1).toLowerCase();
};
