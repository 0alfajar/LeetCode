/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const chunk_arr = []
    for (let i = 0; i < arr.length; i+=size){
        chunk_arr.push(arr.slice(i, i + size))
    }
    return chunk_arr
};
