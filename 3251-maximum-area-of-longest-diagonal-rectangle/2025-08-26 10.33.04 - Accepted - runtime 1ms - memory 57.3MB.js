/**
 * @param {number[][]} dimensions
 * @return {number}
 */
var areaOfMaxDiagonal = function(dimensions) {
        let maxd=0;
        let maxa=0;
        for(lst of dimensions){
            curd=Math.sqrt(lst[0]*lst[0]+lst[1]*lst[1]);
            cura=lst[0]*lst[1];
            if((curd>maxd)||(curd==maxd && maxa<cura)){
                maxd=curd;
                maxa=cura;
            }
        }
        return maxa;
};