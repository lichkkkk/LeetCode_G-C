/**
 * 296. Best Meeting Point
 * Tag: Array
 * Chang Li at UC San Diego
 * Feb. 15, 2016
 */

int minTotalDistance(int** grid, int gridRowSize, int gridColSize) {
    
    int sum = 0;
    int *rowCount = malloc(sizeof(int) * gridRowSize);
    int *colCount = malloc(sizeof(int) * gridColSize);
    memset(rowCount, 0, sizeof(int) * gridRowSize);
    memset(colCount, 0, sizeof(int) * gridColSize);

    // Init
    int i,j;
    for (i = 0; i < gridRowSize; i++) {
        for (j = 0; j < gridColSize; j++) {
            sum += grid[i][j];
            rowCount[i] += grid[i][j];
            colCount[j] += grid[i][j];
        }
    }

    // Find the Column Index
    int res = 0;
    int subsum = 0;
    for (i = 0; i < gridColSize; i++) {
        subsum += colCount[i];
        if (subsum < ((sum+1)/2)) {
            res += subsum;
        } else {
            break;
        }
    }
    int colIndex = i;
    subsum = 0;
    for (i = gridColSize-1; i > colIndex; i--) {
        subsum += colCount[i];
        res += subsum;
    }
    
    // Find the Row Index. Same code as above
    subsum = 0;
    for (i = 0; i < gridRowSize; i++) {
        subsum += rowCount[i];
        if (subsum < ((sum+1)/2)) {
            res += subsum;
        } else {
            break;
        }
    }
    int rowIndex = i;
    subsum = 0;
    for (i = gridRowSize-1; i > rowIndex; i--) {
        subsum += rowCount[i];
        res += subsum;
    }

    free(rowCount);
    free(colCount);
    return res;
}
