/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    for(let i = 0; i < s.length/2 ; i++){
        [s[i], s[s.length-1-i] = [s[s.length-1-i], s[i]];

       // 구조할당 swap
    //    let temp = s[i];
    //    s[i] = s[s.length - 1 - i];
    //    s[s.length - 1 - i] = temp;
        
       
    }
    //리턴 없음
};