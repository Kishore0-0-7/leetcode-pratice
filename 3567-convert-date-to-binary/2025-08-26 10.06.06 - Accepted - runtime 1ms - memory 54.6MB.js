/**
 * @param {string} date
 * @return {string}
 */
var convertDateToBinary = function(date) {
    let lst = date.split("-");
        let year = parseInt(lst[0]).toString(2);
        let month = parseInt(lst[1]).toString(2);
        let day = parseInt(lst[2]).toString(2);
        return `${year}-${month}-${day}`;
};