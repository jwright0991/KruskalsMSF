import heapq
import sys
#Author - Josh Wright
#Kruskals's Programming Assignment
#Reads in a formatted file that contains an edge-weighted directed graph.
#Uses Union-Find data structure with path compression to text for cycles.
#Heapq data structure implemented by adding all the elements to a list and heapifying the list
#unionFind data structure implemented with a list (array). The positions so of the
#list
heap = []

#Returns the parent of x in the UnionFind data structure
#implemented with path compression
def find(unionFind, x):
    if x != unionFind[x]:
        z = find(unionFind,unionFind[x])
        unionFind[x] = z
        return z
    else:
        return x
#returns the source vertex of an edge
def source(edge):
    return edge[1]
#returns the destination vertex of an edge
def destination(edge):
    return edge[2]
#returns the weight of an edge
def weight(edge):
    return edge[0]
#unions two "sets" in the union find data structure
def union(unionFind,source,destination):
    s = find(unionFind, source)
    d = find(unionFind, destination)
    unionFind[s] = d
#check for correct number of commandline arguments
if(len(sys.argv)) == 2:
    #open the file passed in as a commandline argument
    dataFile = open(sys.argv[1], 'r')
    #read the number of vertices from the first line of the file
    size = dataFile.readline()
    size = int(size)
    #Union find data structure.
    #The index represents the vertex, ex v0 = pos 0, v1 = pos 1, etc
    #The value at that position is the parent of the vertex at that position
    #All vertices start out with a self reference, so pos 0 = 0, pos 1 = 1, etc
    unionFind = []
    for i in range(0,size):
        unionFind.append(i)
    #read the lines of the data file in and insert a tuple (weight,vertex1,vertex2) into the heap
    for line in dataFile:
        i = 0
        v1 = ""
        v2 = ""
        w = ""
        #extract the first vertex
        while line[i] != ',':
            v1 += line[i]
            i+=1
        v1 = int(v1)
        i+=1
        #extract the second vertex
        while line[i] != ":":
            v2 += line[i]
            i+=1
        v2 = int(v2)
        i+=1
        #extract the weight of the edge
        while line[i] != "\n":
            w += line[i]
            i+=1
        w = int(w)
        #add the tuple (weight,v1,v2) to the heap
        heap.append((w,v1,v2))
    #close the file
    dataFile.close()
    #call heapify to turn the heap list into a priority queue heap
    heapq.heapify(heap)
    #loop while the heap is not empty
    while heap:
        #remove the smallest edge from the heap
        edge = heapq.heappop(heap)
        #if the parent of the source is not the parent of the destination print the edge and call union on the edge
        if find(unionFind,source(edge)) != find(unionFind,destination(edge)):
            print(str(source(edge)) + ", " + str(destination(edge)) + ":" + str(weight(edge)))
            union(unionFind,source(edge),destination(edge))           
else: #if there was an incorrect number of commandline arguments, print
      #an error message and terminate the program
    print("error: incorrect number of commandline arguments")

