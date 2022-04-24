/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    
    let word = s.split(" ");
    let result = '';
    for(let i = 0; i < word.length; i++){
        result += word[i].split("").reverse().join("") + " ";
        
        }
    
    return result.slice(0, -1);
    
};
