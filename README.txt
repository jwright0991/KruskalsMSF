To run the KruskalsMSF.py file, enter the following command:

python3 KruskalsMSF.py <input file name> 


If the incorrect number of command line arguments is supplied, the program will output an error message and quit, so be sure to supply the correct number of arguments.

The program will read the input file and add each edge to the heap(a list at this point).

After all of the edges are added, the heap(still a list at this point) is heapified.

The union find data structure is implemented on a list(basically an array) and initialized with the position of the list element representing the vertex and the value at that position is an integer value that represents the parent reference of the vertex. For example, a graph with 5 vertex would result in a union find structure initialized as [0,1,2,3,4]

The smallest edge is removed from the heap until it is empty. Every time an edge is removed, it checks to make sure that the parent reference of each edge isn't pointing to the same value, and if that is not the case, it print the edge and call union on the two vertices. Union will update the unionFind data structure to reflect the appropriate new parent reference for one of the vertices.


