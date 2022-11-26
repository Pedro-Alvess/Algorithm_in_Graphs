import pandas as pd

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
            self._vertices.append([str(i),1]) 
    
    @classmethod
    def create_from_matrix(cls,path_csv):
        """
        Create a graph from an adjacence matrix
        """
        df = pd.read_csv(path_csv)
        matrix = df.values.tolist()
        
        G = Graph(len(matrix))

        for v in range(len(matrix)):
            G.label_vertice(v,matrix[v][0])
        
        count = 1
        for v in range(len(matrix)):
            count += 1
            for w in range(len(matrix[v]) - count):
                t = w + count - 1
                if matrix[v][t + 1] > 0:
                    G.add_edge(v,t)
                    G.ponder_edge(v,t,matrix[v][t + 1])
        return G
    
    @classmethod
    def create_from_list(cls,path_csv):
        """
        Create a graph from an adjacence matrix
        """
        df = pd.read_csv(path_csv,header=None)

        list = df.values.tolist()

        G = Graph(len(list))
        
        for v in range(len(list)):
            G.label_vertice(v,list[v][0])

        for v in range(len(list)):
            for w in range(len(list[v]) - 1):

                t = G.__get_vertice_index(list[v][w + 1])
                if G.check_adjacency_between_vertices(v, t) or pd.isna(list[v][w + 1]):
                    break

                G.add_edge(v,t)
        return G


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

    def __get_vertice_index(self,label):
        """
        Private method
        Through the label it returns the index
        """
        for v in self._vertices:
            if v[0] == label:
                return self._vertices.index(v)

    def __get_vertice_label(self,v):
        """
        Private method
        Through the vertice it returns the name of the label
        """
        vertice = self._vertices[v]
        return vertice[0] 

    def label_vertice(self,v,label):
        """
        Add a label to vertice
        """
        if not self.__check_vertice(v):
            raise ValueError(f'Vertice {v} not found')

        if self.__get_vertice_index(label):
            raise ValueError(f'It already exists in vertice with the label {label}')

        self._vertices[v][0] = label
    
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

    def __get_edge_weight(self, v, w):
        if not self.check_adjacency_between_vertices(v,w):
            raise ValueError(f"There is no edge adjacent to {v} and {w}.")
        
        return self._edges[self.__get_edge_index(v,w)][2][0]



    def add_edge(self,v,w):
        """
        Add new edge
        """
        #Checks if the vertical exists
        if not self.__check_vertice(v) or not self.__check_vertice(w):
            raise ValueError(f"Pair of vertices {v} and {w} not found.")


        #Checks for parallel edges
        if self.check_adjacency_between_vertices(v,w):
            raise TypeError("The Graph library does not support parallel edges.")

        #Checks the existence of loops
        if v == w:
            raise TypeError("The Graph library does not support loops")
        
        self._edges.append([v,w,[1,""]])
    
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
    
    def check_adjacency_between_edges(self, edge_1: list, edge_2: list):
        """
        Check adjaceny between edges 
        """

        for v in range(2):
            for w in range(2):
                if edge_1[v] == edge_2[w]:
                    return True

        return False
    
    def check_adjacency_between_vertices(self,v,w):
        """
        Check adjaceny between vertices
        """
        return self.__get_edge_index(v,w) >= 0
    
    def existing_edges(self,v):
        """
        Return all edges adjacent to vertice v
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
        Creates an adjacency list starting from the graph
        """
        aux_list = []
        adjacency_list = []

        for vertice in range(self.len_vertices):

            label_name = self.__get_vertice_label(vertice)
            aux_list.append(label_name)

            for edge in self.existing_edges(vertice):
                if edge[0] != label_name:
                    aux_list.append(edge[0])
                else:
                    aux_list.append(edge[1])
           
            adjacency_list.append(aux_list)
            aux_list = []
        
        return adjacency_list
    
    def show_adjacency_list(self):
        """
        Show adjacency list
        """
        aux_list = self.adjacency_list()

        for line in aux_list:
            for vertice in line:
                print(vertice, end= "")
                
                if line.index(vertice) < len(line) - 1:
                    print(" --> ", end= "")
            print() 

    def adjacency_list_to_csv(self, file_name = 'Graph'):
        """
         Transform the adjacency list into csv
        """
        df = pd.DataFrame(data = self.adjacency_list())
        df.to_csv(file_name + '.csv',header= False, index= False)

    def adjacency_matrix(self):
        """
        Creates an adjacency matrix starting from the graph
        """
        aux_list = []
        matrix = []

        for vertice in range(self.len_vertices):
            aux_list.append(self.__get_vertice_label(vertice))
        
        matrix.append(aux_list)
        aux_list = []

        for v in range(len(self._vertices)):
            aux_list.append(self.__get_vertice_label(v))

            for w in range(len(self._vertices)):
                if self.check_adjacency_between_vertices(v,w):
                    aux_list.append(self.__get_edge_weight(v,w))
                else:
                    aux_list.append(0)

            matrix.append(aux_list)
            aux_list = []
        
        return matrix

    def __create_adjacency_matrix(self):
        """
        Private Class
        Create adjacency matriz
        """
        self._df = {}
        matrix = self.adjacency_matrix()
        
        for x in range(len(matrix) - 1):
            self._df[matrix[0][x]] = matrix[x + 1][1:]
        
        self._df = pd.DataFrame(data = self._df, index = self.adjacency_matrix()[0])

    def show_adjacency_matrix(self):
        """
        Show adjacency matrix
        """
        self.__create_adjacency_matrix()
        print(self._df)
    
    def adjacency_matrix_to_csv(self,file_name = 'Graph'):
        """
        Transform the adjacency matrix into csv
        """
        self.__create_adjacency_matrix()
        self._df.to_csv(file_name + '.csv')



    #Função de teste
    @property
    def show(self):
        print("Vertices: ",self._vertices) 
        print("Edges: ",self._edges)

#Area de teste

# Graph.create_from_list('lista.csv')
# Graph.create_from_matrix('Graph.csv')

# G = Graph(5)
# G.existing_edges
# G.label_vertice(0,"A")
# G.label_vertice(1,"B")
# G.label_vertice(2,"C")
# G.label_vertice(3,"D")
# G.label_vertice(4,"E")
# G.add_edge(0,1)
# G.add_edge(0,2)
# G.add_edge(3,4)
# G.ponder_edge(0,2,3)
# G.ponder_edge(0,1,900)
# #G.add_edge(1,2)

# G.show
# G.label_edge(0,2,"E51")
# G.ponder_edge(0,2,3)
# G.show


# print()
# print(G.adjacency_list())
# G.show_adjacency_list()
# print(G.adjacency_matrix())
# G.show_adjacency_matrix()
# print()
# G.adjacency_list_to_csv(file_name='lista')
# G.adjacency_matrix_to_csv()
# print(G.check_adjacency_between_edges([0,2],[0,55]))

