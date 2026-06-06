/**
 * @param {number} target
 * @return {number}
 */
var reachNumber = function(target) {
    target=Math.abs(target);
        let steps=0,moves=0;
        while (steps<target || (steps-target)%2!==0) {
            moves++;
            steps+=moves;
        }
        return moves;
};