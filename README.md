# Trabalho_Pratico_Algoritmo_Grafos

# Graph()

class **Graph(n)**

Cria um grafo com n vértices, com rótulos padrões de acordo com a ordem de inicialização do vértice. Apresenta erro caso o valor n seja menor ou igual a 0.

**parâmetro:** n : int
Número inteiro que representa a quantidade de vértices a serem inicializados.

**Big O:** n

# Graph().create_from_matrix

Método de classe **Graph.create_from_matrix(path_csv)**

Cria um grafo a partir de uma matriz de adjacência contida em uma csv. 

**parâmetro:** path_csv : str
			Caminho do arquivo CSV ou apenas o nome do arquivo (caso esteja na mesma pasta do código).

**retorna:** Objeto de classe iterável do tipo Graph

**Big O:** 
- Melhor caso : n
- Caso médio : n^2
- Pior caso : n^2

**Exemplo:** 
```
Graph.create_from_matrix('Graph.csv').show
```

**Entrada:** 
```
Graph.csv :
  ,A,B,C,D,E
  A,0,900,3,0,0
  B,900,0,0,0,0
  C,3,0,0,0,0
  D,0,0,0,0,1
  E,0,0,0,1,0
```

**Saída:** 
```
Vertices:  [['A', 1], ['B', 1], ['C', 1], ['D', 1], ['E', 1]]
Edges:  [[0, 1, [900, '']], [0, 2, [3, '']], [3, 4, [1, '']]]
```

# Graph().create_from_list

Método de classe **Graph.create_from_list(path_csv)**

Cria um grafo a partir de uma lista de adjacência contida em uma csv. 

**parâmetro:** path_csv : str
			Caminho do arquivo CSV ou apenas o nome do arquivo (caso esteja na mesma pasta do código).

**retorna:** Objeto de classe iterável do tipo Graph

**Big O:** n^2

**Exemplo:** 
```
Graph.create_from_list('Lista.csv').show
```

**Entrada:**
```
Lista.csv : 
  A,B,C
  B,A,
  C,A,
  D,E,
  E,D,
```

**Saída:** 
```
Vertices:  [['A', 1], ['B', 1], ['C', 1], ['D', 1], ['E', 1]]
Edges:  [[0, 1, [900, '']], [0, 2, [3, '']], [3, 4, [1, '']]]
```

# __check_vertice

Método privado **__check_vertice(v)**

Verifica a existência de um vértice dentro de um tipo de objeto Graph

**parâmetro:** v : int
		Número inteiro que representa a posição do vértice. 
**retorna:** bool

**Big O:** 1

# __get_edge_index

Método privado **__get_edge_index(v,w)**

Recupera o index de uma aresta dentro da variável privada Graph._edges.

**parâmetro:** v : int
		Número inteiro que representa a posição de um vértice. 
	        w : int 
Número inteiro que representa a posição de um vértice. 
**retorna:** int

**Big O:** 
- Melhor caso : 1
- Caso médio : n
- Pior caso : n


# __get_vertice_index

Método privado **__get_vertice_index(label)**

Por meio de um rótulo, retorna a posição do vértice

**parâmetro:** label : str
		String contendo um rótulo/nome de um possível vértice.
**retorna:** int

**Big O:** 
- Melhor caso : 1
- Caso médio : n
- Pior caso : n


# __get_vertice_label

Método privado **__get_vertice_label(v)**

Por meio do index do vértice, retorna o seu rótulo.

**parâmetro:** v : int
		Número inteiro que representa a posição do vértice. 
**retorna:** int

**Big O:** 1


# Graph().label_vertice

Método de classe **label_vertice(v,label)**

Adiciona um rótulo ao vértice v. Apresenta erro caso o vértice v não seja encontrado. 

**parâmetro:** v : int
		Número inteiro que representa a posição do vértice. 
	        label : str
		String que representa o rótulo a ser inserido no vértice v.

**Big O:** 1



# Graph().label_edge

Método de classe **label_edge(v,w,label)**

Adiciona um rótulo a aresta adjacente a v e w. Apresenta uma mensagem de aviso, caso o não exista uma aresta adjacente a v e w.

**parâmetro:** v : int
		Número inteiro que representa a posição do vértice. 
 	        w : int 
Número inteiro que representa a posição do vértice. 
	        label : str
		String que representa o rótulo a ser inserido na aresta.

**Big O:** 1


# Graph().ponder_edge

Método de classe **ponder_edge(v,w,weight)**

Adiciona um peso a aresta adjacente a v e w. Apresenta uma mensagem de erro, caso o não exista uma aresta adjacente a v e w.

**parâmetro:** v : int
		Número inteiro que representa a posição do vértice. 
 	        w : int 
Número inteiro que representa a posição do vértice. 
	        weight : str
		String que representa o rótulo a ser inserido no vértice v.

**Big O:** 1


# __get_edge_weight

Método privado __get_edge_weight(v,w)

Retorna o peso da aresta adjacente a v e w. Apresenta uma mensagem de erro, caso o não exista uma aresta adjacente a v e w.

**parâmetro:** v : int
		Número inteiro que representa a posição de um vértice. 
	        w : int 
Número inteiro que representa a posição de um vértice. 

**retorna:** int

**Big O:** 1


# Graph().add_edge

Método de classe **add_edge(v,w)**

Adiciona uma aresta adjacente ao vértice v e w. Apresenta uma mensagem de erro, caso:
v e/ou w não exista dentro do objeto de classe Graph;
Já exista uma aresta adjacente a v e w;
v e w forem iguais;

**parâmetro:** v : int
		Número inteiro que representa a posição do vértice. 
 	        w : int 
Número inteiro que representa a posição do vértice. 

**Big O:** 1


# Graph().remove_edge

Método de classe **remove_edge(v,w)**

Deleta a aresta adjacente ao vértice v e w. Apresenta uma mensagem de erro, caso não exista uma aresta adjacente ao vértice v e w.

**parâmetro:** v : int
		Número inteiro que representa a posição do vértice. 
 	        w : int 
Número inteiro que representa a posição do vértice. 

**Big O:** 1


# Graph().len_vertices

Propriedade **len_vertices**

Retorna a quantidade de vértices dentro do grafo contido no objeto de classe Graph.

**Retorna:** int

**Big O:** 1

**Exemplo:**
```
G = Graph(5)
print(G.len_vertices)
```

**Saída:** 5


# Graph().len_edges

Propriedade **len_edeges**

Retorna a quantidade de arestas dentro do grafo contido no objeto de classe Graph.

**Retorna:** int

**Big O:** 1

**Exemplo:**
```
G = Graph(5)
G.add_edge(0,1)
G.add_edge(1,4)
print(G.len_edges)
```

**Saída:** 2


# Graph().check_empty_graph

Propriedade **check_empty_graph**

Verifica se o grafo está vazio.

**Retorna:** bool

**Big O:** 1

**Exemplo:**
```
G = Graph(5)
G.add_edge(0,2)
G.add_edge(1,3)
print(G.check_empty_graph)
```

**Saída:** False


# Graph().check_full_graph

Propriedade **check_full_graph**

Verifica se o grafo está completo.

**Retorna:** bool

**Big O:** 1

**Exemplo:**
```
G = Graph(2)
G.add_edge(0,1)
print(G.check_full_graph)
```

**Saída:** True


# Graph().check_adjacency_between_edges

Método de classe **check_adjacency_between_edges(edge_1 : list, edge_2 : list)**

Verifica a adjacência entre arestas.

**parâmetro:** edge_1 : list
		Lista contendo dois números inteiros. 
 	        edge_2 : list 
Lista contendo dois números inteiros. 

**Retorna:** bool

**Big O:** 1

**Exemplo:**
```
G = Graph(3)
G.add_edge(0,1)
G.add_edge(2,1)
print(G.check_adjacency_between_edges([0,1],[1,2]))
```

**Saída:** True


# Graph().check_adjacency_between_vertices

Método de classe **check_adjacency_between_vertices(v, w)**

Verifica a adjacência entre vértices.

**parâmetro:** v : int
		Número inteiro que representa a posição do vértice. 
 	        w : int 
Número inteiro que representa a posição do vértice.  

**Retorna:** bool

**Big O:** 1

**Exemplo:**
```
G = Graph(3)
G.add_edge(0,1)
print(G.check_adjacency_between_vertices(0,1))
```

**Saída:** True


# Graph().existing_edges

Método de classe **existing_edges(v)**

Retorna todas as arestas adjacentes a v. Apresenta um aviso caso não exista nenhuma aresta adjacente a v. 

**parâmetro:** v : int
		Número inteiro que representa a posição do vértice.   

**retorna:** list

**Big O:** n

**Exemplo:**
```
G = Graph(3)
G.add_edge(0,1)
G.ponder_edge(0,1,52)
G.label_edge(0,1,'E1')

print(G.existing_edges(0))
```

**Saída:** [['0', '1', [52, 'E1']]]


# Graph().adjacency_list

Método de classe **adjacency_list()**

Retorna uma lista de adjacência. 

**Retorna:** list

**Big O:** n2

**Exemplo:**
```
G = Graph(3)
G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(2,1)
 
print(G.adjacency_list())
```

**Saída:** 
```
[['0', '1', '2'], ['1', '0', '2'], ['2', '0', '1']]
```


# Graph().show_adjacency_list

Método de classe **show_adjacency_list()**

Imprime a lista de adjacência. 

**Big O:** n2

**Exemplo:**
```
G = Graph(3)
G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(2,1)
 
G.show_adjacency_list
```

Saída: 
```
0 --> 1 --> 2
1 --> 0 --> 2
2 --> 0 --> 1
```

# Graph().adjacency_list_to_csv

Método de classe **adjacency_list_to_csv(file_name = ‘Graph’)**

Transforma a lista de adjacência em um arquivo csv. Caso não seja passado o nome do arquivo no parâmetro, por padrão o arquivo será gerado com o nome de “Graph.csv”.

**parâmetro:** file_name : str
		String referente ao nome do arquivo, não é necessário passar o “.csv”
 junto ao nome.   

**Big O:** 1


# Graph().adjacency_matrix

Método de classe **adjacency_matrix()**

Retorna uma matriz de adjacência. 

**Retorna:** list

**Big O:** n2

**Exemplo:**
```
G = Graph(3)
G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(2,1)
 
print(G.adjacency_matrix())
```

**Saída:** 
```
[['0', '1', '2'], ['0', 0, 1, 1], ['1', 1, 0, 1], ['2', 1, 1, 0]]
```

O primeiro índice da lista é referente ao “cabeçalho” da matriz, e todas as lista dentro da lista principal, após a primeira lista, possuem uma string referente a “coluna” 1 da matriz.


# __create_adjacency_matrix

Método privado **__create_adjacency_matrix()**

Cria uma matriz de adjacência 

**Big O:** n


# Graph().show_adjacency_matrix

Método de classe **show_adjacency_matrix()**

Imprime a matriz de adjacência. 

**Big O:** 1

**Exemplo:**
```
G = Graph(3)
G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(2,1)
 
G.show_adjacency_matrix
```

**Saída:**
```
   0  1  2
0  0  1  1
1  1  0  1
2  1  1  0
```

# Graph().adjacency_matrix_to_csv

Método de classe **adjacency_list_to_csv(file_name = ‘Graph’)**

Transforma a matriz de adjacência em um arquivo csv. Caso não seja passado o nome do arquivo no parâmetro, por padrão o arquivo será gerado com o nome de “Graph.csv”.

**parâmetro:** file_name : str
		String referente ao nome do arquivo, não é necessário passar o “.csv”
 junto ao nome.   

**Big O:** 1



# Graph().show

Método de **classe show()**

Imprime uma lista de vértices e arestas.

**Big O:** 1

