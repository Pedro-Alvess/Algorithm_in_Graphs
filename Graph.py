class Graph():
    def __init__(self,n):
        """
        Constructor method
        Initializes the class with the number of vertices n
        """
        if n <= 0:
            raise ValueError(f"{n} is not a valid value. Try a value greater than 0.")

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

    def __get_vertice_label(self,v):
        """
        Private method
        Get the label name if exists
        """
        label_name = self._vertices[v]

        if label_name == "":
            return str(v)
        else:
            return label_name  

    def label_vertice(self,v,label):
        """
        Add a label to vertice
        """
        if not self.__check_vertice(v):
            raise ValueError(f"Vertice {v} not found")

        self._vertices[v] = label
    
    def label_edge(self,v,w,label):
        """
        Add a label to edge
        """
        index = self.__get_edge_index(v,w)

        if index >= 0:
            self._edges[index][2][1] = label  

        else:
            print(f"Warning: There is no edge adjacent to {v} and {w}.")
        
    def ponder_edge(self,v,w,weight):
        """
        Add a weight to edge
        """
        index = self.__get_edge_index(v,w)

        if index >= 0:
            self._edges[index][2][0] = weight  

        else:
            raise ValueError(f"There is no edge adjacent to {v} and {w}.")


    def add_edge(self,v,w):
        """
        Add new edge
        """
        #Checks if the vertical exists
        if not self.__check_vertice(v) or not self.__check_vertice(w):
            raise ValueError(f"Value Error: Pair of vertices {v} and {w} not found.")


        #Checks for parallel edges
        if self.check_adjacency(v,w):
            raise TypeError("The Graph library does not support parallel edges.")

        #Checks the existence of loops
        if v == w:
            raise TypeError("The Graph library does not support loops")
        
        self._edges.append([v,w,[0,""]])
    
    def remove_edge(self,v,w):
        """
        Remove edges
        """
        index = self.__get_edge_index(v,w)

        if index >= 0:
            del self._edges[index]
        else:
            raise ValueError(f"There is no edge adjacent to {v} and {w}")

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
    
    @property
    def check_empty_graph(self):
        """
        Property
        Check if the graph is empty
        """
        return not self._edges
    
    @property
    def check_full_graph(self):
        """
        Property
        Check if the graph is full
        """
        n = len(self._vertices)
        if len(self._edges) == (n * (n - 1)) / 2:
            return True

        return False
    
    def check_adjacency(self,v,w):
        """
        Check adjaceny between vertices
        """
        return self.__get_edge_index(v,w) >= 0 or self.__get_edge_index(w,v) >= 0
    
    def existing_edges(self,v):
        """
        Return all edges adjacent to vertical v
        """
        edge_list = []

        for edge in self._edges:
            if edge[0] == v or edge[1] == v:
                edge_list.append([self.__get_vertice_label(edge[0]),self.__get_vertice_label(edge[1]),edge[2]])
        
        if not edge_list:
            print(f"Theres is no edge adjacent to the vertice {v}")

        
        return edge_list
    
    def adjacency_list(self):
        """

        """
        aux_list = []
        adjacency_list = []

        for vertice in range(self.len_vertices):

            label_name = self.__get_vertice_label(vertice)
            aux_list.append(label_name)
            print(f"esta em {label_name} e vertice {vertice}")

            for edge in self.existing_edges(vertice):
                print("teste ",edge)
                if edge[0] != label_name:
                    aux_list.append(edge[0])
                else:
                    aux_list.append(edge[1])
           
            adjacency_list.append(aux_list)
            aux_list = []
        
        return adjacency_list

    #Função de teste
    @property
    def show(self):
        print(self._vertices) 
        print(self._edges)

#Area de teste
G = Graph(4)
G.label_vertice(0,"A")
G.label_vertice(1,"B")
G.label_vertice(2,"C")
G.label_vertice(3,"D")
#G.label_vertice(4,"E")
G.add_edge(0,1)
G.add_edge(0,2)
#G.add_edge(1,2)
G.show
G.label_edge(0,2,"E51")
G.ponder_edge(0,2,3)
G.show
print(G.existing_edges(1))
print(G.adjacency_list())





