/**
 * 335. Self Crossing
 * Tag: State Machine?
 * Chang Li at UC San Diego
 * Feb. 25, 2016
 */

bool isSelfCrossing(int* x, int xSize) {

    int i;
    
    // Expand from inner space to outer space at first
    for (i = 2; i < xSize && x[i] > x[i-2]; i++);
    
    // Judge if the state transfer is legal 
    if ((++i < xSize) && ((i > 4) || (i==4 && x[i-1]==x[i-3])) && (x[i]+x[i-4] >= x[i-2])) return true;
    
    // Shrink from outer space to inner space
    for (; i < xSize && x[i] < x[i-2]; i++);
    
    return (i < xSize);

}
