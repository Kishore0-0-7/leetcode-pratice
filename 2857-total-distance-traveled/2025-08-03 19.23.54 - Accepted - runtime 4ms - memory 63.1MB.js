/**
 * @param {number} mainTank
 * @param {number} additionalTank
 * @return {number}
 */
var distanceTraveled = function(a, b) {
    return (a + Math.min(Math.floor((a - 1) / 4), b)) * 10;
};