class Graphs():
    #Initializes the class with the number of vertices n
    def __init__(self,n):
        self._vertices = []
        self._edges = []
        for i in range(n):
            self._vertices.append("") 
    
    #Checks the existence of a vertice on the graph G
    def __check_vertice(self,v):
        return 0 <= v < len(self._vertices)

    #Add a label to vertice
    def label_vertice(self,v,label):
        if not self.__check_vertice(v):
            print(f"Vertice {v} not found")
            return

        self._vertices[v] = label

    #Add new edge
    def add_edge(self,v,w):
        print(self.__check_vertice(v))
        if not self.__check_vertice(v) or not self.__check_vertice(w):
            print(f"Pair of vertices {v} and {w} not found")
            return

        self._edges.append([v,w])
    
    def remove_edge(self,v,w):
        if not self.__check_vertice(v) or not self.__check_vertice(w):
            print(f"Pair of vertices {v} and {w} not found")
            return
        
        try:
            self._edges.remove([v,w])
        except:
            print(f"There is no edge adjacent to {v} and {w}")



    def show(self):
        print(self._vertices) 
        print(self._edges)



G = Graphs(5)
G.add_edge(0,2)
G.show()
G.remove_edge(6,2)
G.show()