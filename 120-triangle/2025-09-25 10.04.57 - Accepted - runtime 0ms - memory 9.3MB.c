int minimumTotal(int** triangle, int triangleSize, int* triangleColSize) {
    for (int i=triangleSize-2;i>=0;i--) {
            for (int j=0;j<triangleColSize[i];j++) {
                int down=triangle[i+1][j];
                int diag=triangle[i+1][j+1];
                triangle[i][j]+=down<diag?down:diag;
            }
        }
        return triangle[0][0];
}