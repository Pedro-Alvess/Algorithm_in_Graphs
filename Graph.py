class Graph():
    def __init__(self,n):
        """
        Constructor method
        Initializes the class with the number of vertices n
        """
        self._vertices = []
        self._edges = []
        for i in range(n):
            self._vertices.append("") 
     
    def __check_vertice(self,v):
        """
        Private method
        Checks the existence of a vertice on the graph G
        """
        return 0 <= v < self.len_vertices

    def __get_edge_index(self,v,w):
        """
        Private method
        Get the index of edge
        """
        for edge in self._edges:
            if edge[0] == v and edge[1] == w or edge[0] == w and edge[1] == v:
                return self._edges.index(edge)
        return -1    

    def label_vertice(self,v,label):
        """
        Add a label to vertice
        """
        if not self.__check_vertice(v):
            print(f"Vertice {v} not found")
            return

        self._vertices[v] = label
    
    def label_edge(self,v,w,label):
        """
        Add a label to edge
        """
        index = self.__get_edge_index(v,w)

        if index >= 0:
            self._edges[index][2][1] = label  

        else:
            print(f"There is no edge adjacent to {v} and {w}")
        
    def ponder_edge(self,v,w,weight):
        """
        Add a weight to edge
        """
        index = self.__get_edge_index(v,w)

        if index >= 0:
            self._edges[index][2][0] = weight  

        else:
            print(f"There is no edge adjacent to {v} and {w}")


    def add_edge(self,v,w):
        """
        Add new edge
        """
        if not self.__check_vertice(v) or not self.__check_vertice(w):
            print(f"Pair of vertices {v} and {w} not found")
            return

        self._edges.append([v,w,[0,""]])
    
    def remove_edge(self,v,w):
        """
        Remove edges
        """
        index = self.__get_edge_index(v,w)

        if index >= 0:
            del self._edges[index]
        else:
            print(f"There is no edge adjacent to {v} and {w}")

    @property
    def len_vertices(self):
        """
        Property
        Get the number of vertices
        """
        return len(self._vertices)
    
    @property
    def len_edges(self):
        """
        Property
        Get the number of edges
        """
        return len(self._edges)
    
    def check_adjacency(self,v,w):
        """
        Check adjaceny between vertices
        """
        return self.__get_edge_index(v,w) >= 0
    
   

    @property
    def show(self):
        print(self._vertices) 
        print(self._edges)


G = Graph(5)
G.add_edge(0,2)
G.add_edge(4,2)
G.show
G.label_edge(0,2,"dado")
G.ponder_edge(0,2,3)
G.show
G.remove_edge(2,0)
G.show




