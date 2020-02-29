from node import Noh

class Jogo:
  def __init__(self,size):
    # Inicialize o tamanho do quebra-cabeça pelo tamanho especificado em size, 
    # cria as listas aberta e fechada 
    # inicio (start) e objetivo (goal)
    # movimentos para chegar na solução
    self.n = size
    self.open = []
    self.closed = []
    self.start = []
    self.goal = []
    self.movimentos = 0

  def inicio(self):
    self.start = []
    self.goal = [['1','2','3'],['4','5','6'],['7','8','0']]

    print("Entre com a matriz inicial do jogo:")
    for i in range(0,self.n):
      temp = input().split(" ")
      self.start.append(temp)

    #print("Entre com a matriz objetivo do jogo:")
    #for i in range(0,self.n):
    #  temp = input().split(" ")
    #  self.goal.append(temp)
    print("--------------------")
          
  def h(self, estado_atual):
    # Heuristica: conta diferenças entre o estado atual e o objetivo
    contador = 0
    for i in range(0,self.n):
        for j in range(0,self.n):
            if estado_atual[i][j] != self.goal[i][j]:
                contador += 1
    return contador

  def f(self, noh):
    # Função de avaliação: f(x) = h(x) + g(x)
    # heurística + custo
    # custo é igual a profundidade do nó
    return self.h(noh.state) + noh.level

  def imprime(self, estado_atual):
    print()
    print(" \\/ ")
    print()
    for i in estado_atual:
        for j in i:
            print(j, end=" ")
        print()

  def solucao(self, noh):
    print("Caminho da solução:")
    while noh.pai != None:
      self.imprime(noh.state)
      noh = noh.pai
      self.movimentos+=1
    self.imprime(self.start)
     

  def busca(self):
    noh_inicial = Noh(self.start, 0, 0, None)
    noh_inicial.fval = self.f(noh_inicial)
    # coloca o nó inicial na lista aberta
    self.open.append(noh_inicial)
    while True:
      print("-------------")
      noh_atual = self.open[0]
      self.imprime(noh_atual.state)
      print('h:', self.h(noh_atual.state))
      print('f:', self.f(noh_atual))
      print('level', noh_atual.level)
      # Se a diferença entre o nó atual e o objetivo for 0, o nó objetivo foi encontrado
      if(self.h(noh_atual.state) == 0):
          self.solucao(noh_atual)
          break
      filhos = noh_atual.gerar_filhos(self.closed)
      for i in filhos:
          i.fval = self.f(i)
          self.open.append(i)
          self.imprime(i.state)
          print('h:', self.h(i.state))
          print('f:', self.f(i))
          print('level', i.level)
          print("-------------")
      self.closed.append(noh_atual)
      del self.open[0]
      #input()

      """ sort the open list based on f value """
      self.open.sort(key = lambda x:x.fval,reverse=False)

    print()
    print("Nós abertos:", len(self.closed) + len(self.open))
    print("Quantidade de movimentos: ", self.movimentos)