#HELENA KUCHINSKI FERREIRA
#Sua tarefa será construir um heap (binário, max-heap), e criar métodos para criar a árvore e apartir de um array, inserir, excluir, e buscar valores na árvore. Seu objetivo é explicar o funcionamentodos métodos que você irá criar. Para isso, deve buscar em sites acadêmicos, exemplos deimplementação de árvores heap.Para testar, você deve usar um array com, no mínimo, 500 itens, gerados randomicamente ecriar métodos para testar se a estrutura criada obedece a regra de criação que você determinou.

import numpy as np

class Heap:
  def __init__(self, size):
    self.heapSize = 0 #armazena no n° de elementos no heap
    self.maxSize = size + 1 #o tamanho máximo (+1 porque o primeiro elemento é deixado vazio)
    self.list = (size+1) * [None] #inicializa a lista

#Função para retornar a raiz da árvore 
def peekofHeap(rootNode):
  if not rootNode:  #se não for o nó raiz
    return
  else:  #se for o nó raiz
    return rootNode.list[1] 

#Função para achar o tamanho do Heap
def sizeofHeap(rootNode):
  if not rootNode:
    return
  else:
    return rootNode.heapSize #retorna o tamanho do heap

#Função para ordenar os nós do heap
def levelOrder(rootNode):
  if not rootNode:
    return
  else:
    for i in range(1, rootNode.heapSize+1): #pega cada elemento da lista e imprime o mesmo
      print(rootNode.list[i])

#Função que troca recursivamente a posição do nó recém-adicionado com seus nós adjacentes. Este processo continua até que o nó inserido seja colocado em sua posição correta dentro do heap, pois é necessário que a estrutura do heap continue a mesma depois de excluir um nó
def treeInsert(rootNode, index, heapType):
  parentIndex = int(index/2) #index do pai
  if index <= 1:
    return
  if heapType == "Min":
    if rootNode.list[index] < rootNode.list[parentIndex]:
      listNode = rootNode.list[index]
      rootNode.list[index] = rootNode.list[parentIndex]
      rootNode.list[parentIndex] = listNode
    treeInsert(rootNode, parentIndex, heapType)
  elif heapType == "Max":
    if rootNode.list[index] > rootNode.list[parentIndex]:
        listNode = rootNode.list[index]
        rootNode.list[index] = rootNode.list[parentIndex]
        rootNode.list[parentIndex] = listNode
    treeInsert(rootNode, parentIndex, heapType)

#Função para inserir um nó
def insertNode(rootNode, nodeValue, heapType):
  if rootNode.heapSize + 1 == rootNode.maxSize:#confere se o heap não está com o valor máximo
    return "O Heap está cheio."
  rootNode.list[rootNode.heapSize + 1] = nodeValue #adiciona o valor no heap
  rootNode.heapSize += 1
  treeInsert(rootNode, rootNode.heapSize, heapType) #insere o valor no lugar correto
  return "O nó foi inserido com sucesso."

#Função que troca recursivamente a posição do nó recém-adicionado com seus nós adjacentes. Este processo continua até que o nó inserido seja colocado em sua posição correta dentro do heap, pois é necessário que a estrutura do heap continue a mesma depois de excluir um nó
def treeExtract(rootNode, index, heapType):
  leftIndex = index * 2 #define index do nó esquerdo
  rightIndex = index * 2 + 1 #define index do nó direito
  child = 0

  if rootNode.heapSize < leftIndex:
    return
  elif rootNode.heapSize == leftIndex:
    if heapType == "Min":
      if rootNode.list[index] > rootNode.list[leftIndex]:
        listNode = rootNode.list[index]
        rootNode.list[index] = rootNode.list[leftIndex]
        rootNode.list[leftIndex] = listNode
      return
    else:
      if rootNode.list[index] < rootNode.list[leftIndex]:
        listNode = rootNode.list[index]
        rootNode.list[index] = rootNode.list[leftIndex]
        rootNode.list[leftIndex] = listNode
      return

  else:
    if heapType == "Max":
      if rootNode.list[leftIndex] < rootNode.list[rightIndex]:
        child = leftIndex
      else:
        child = rightIndex
      if rootNode.list[index] > rootNode.list[child]:
        listNode = rootNode.list[index]
        rootNode.list[index] = rootNode.list[child]
        rootNode.list[child] = listNode
    else:
      if rootNode.list[leftIndex] > rootNode.list[rightIndex]:
        child = leftIndex
      else:
        child = rightIndex
      if rootNode.list[index] < rootNode.list[child]:
        listNode = rootNode.list[index]
        rootNode.list[index] = rootNode.list[child]
        rootNode.list[child] = listNode
  treeExtract(rootNode, child, heapType) #insere o valor no lugar correto

#Função para excluir um nó do heap
def extractNode(rootNode, heapType):
  if rootNode.heapSize == 0:
    return "O heap está vazio."
  else:
    extractedNode = rootNode.list[1]
    rootNode.list[1] = rootNode.list[rootNode.heapSize]
    rootNode.list[rootNode.heapSize] = None
    rootNode.heapSize -= 1
    treeExtract(rootNode, 1, heapType)
    return extractedNode

#Inicialiazando Heap
newHeap = Heap(20)
heap = np.random.randint(low=1, high=1000, size=500).tolist()
for i in heap:
  insertNode(newHeap, i, "Max")
    
levelOrder(newHeap)
print("------------------------")
extractNode(newHeap, "Max")
levelOrder(newHeap)

#Após os testes cloncui que meu método está sendo exceutado de forma correta
