/**
 * @param {number} n
 * @return {number[]}
 */
var lexicalOrder = function(n) {
    var num = []
    for (var i = 1, i <= n, i++){
        num.push(i)
    }
    return num.sort()
};