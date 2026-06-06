/**
 * @param {number[][]} polets
 * @return {number}
 */
var largestTriangleArea = function(polets) {
    let max_area=0.0;
    for (let i=0; i<polets.length; ++i) {
        for (let j=i+1; j<polets.length; ++j) {
            for (let k=j+1; k<polets.length; ++k) {
                let x1=polets[i][0],y1=polets[i][1];
                let x2=polets[j][0],y2=polets[j][1];
                let x3=polets[k][0],y3=polets[k][1];
                let area=0.5*Math.abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2));
                if (area > max_area) {
                    max_area=area;
                }
            }
        }
    }
    return max_area;
};