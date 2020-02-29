class Noh:
  def __init__(self,estado,nivel,fval, pai):
    # Inicialize o nó com os dados, o nível do nó (profundidade) e o f calculado
    self.state = estado
    self.level = nivel
    self.fval = fval
    self.pai = pai

  def find(self,puz,x):
    # função usada para achar o espaço vazio ou 0
    for i in range(0,len(self.state)):
        for j in range(0,len(self.state)):
            if puz[i][j] == x:
                return i,j

  def gerar_filhos(self, closed):
    # Gera nós filhos a partir do nó fornecido movendo o espaço em branco nas quatro direções [para cima, para baixo, esquerda, direita]
    x,y = self.find(self.state,'0')
    # val_list contém valores de posição para mover o espaço em branco em qualquer uma das 4 direções [para cima, para baixo, esquerda, direita], respectivamente
    val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
    children = []
    for i in val_list:
      child = self.shuffle(self.state,x,y,i[0],i[1])
      if child is not None:
        child_node = Noh(child,self.level+1,0, self)
        existe = 0
        for noh in closed:
          if child_node.state == noh.state:
            existe = 1
            break
        if existe != 1:
          children.append(child_node)
    return children
      
  def shuffle(self,puz,x1,y1,x2,y2):
    # Move o espaço em branco na direção especificada e, se o valor da posição estiver fora dos limites, retorna None (Nenhum)
    if x2 >= 0 and x2 < len(self.state) and y2 >= 0 and y2 < len(self.state):
        temp_puz = []
        temp_puz = self.copy(puz)
        temp = temp_puz[x2][y2]
        temp_puz[x2][y2] = temp_puz[x1][y1]
        temp_puz[x1][y1] = temp
        return temp_puz
    else:
        return None
          
  def copy(self,root):
    # gera uma cópia da matriz original
    temp = []
    for i in root:
        t = []
        for j in i:
            t.append(j)
        temp.append(t)
    return temp    
          

