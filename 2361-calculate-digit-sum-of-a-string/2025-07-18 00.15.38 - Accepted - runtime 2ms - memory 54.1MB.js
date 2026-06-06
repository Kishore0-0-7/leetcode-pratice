/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var digitSum = function(s, k) {
     while (s.length > k) {
            let new_s = '';
            for (let i = 0; i < s.length; i += k) {
                let sum = 0;
                for (let j = i; j < Math.min(i + k, s.length); j++) {
                    sum += parseInt(s[j]);
                }
                new_s += sum.toString();
            }
            s = new_s;
        }
        return s;
};