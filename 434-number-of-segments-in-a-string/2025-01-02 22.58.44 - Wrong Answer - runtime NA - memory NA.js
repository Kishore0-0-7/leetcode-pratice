var countSegments = function(s) {
    if(s === null||s=== undefined ||s.trim() === "") return 0;
    let a=s.split(" ");
        return a.length;
};