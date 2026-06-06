var countSegments = function(s) {
    s = s.trim();
    if (s === "") {
        return 0;
    }
    let segments = s.split(' ');
    return segments.length;
};