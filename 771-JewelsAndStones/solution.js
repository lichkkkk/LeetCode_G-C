/**
 * @param {string} J
 * @param {string} S
 * @return {number}
 */
var numJewelsInStones = function(J, S) {
    let count = 0;
    let jset = J.split("");
    let slist = S.split("");
    for (s in slist) {
        if (jset.includes(slist[s])) {
            count += 1;
        }
    }
    return count;
};
