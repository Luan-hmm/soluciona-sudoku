#Solucionador de Sudoku

#Sudoku a solucionar

tabela = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def resolve(ta):
    procura = procura_0(ta)
    if not procura:
        return True
    else:
        row, col = procura
        
    for i in range(1,10):
        if valid(ta, i, (row, col)):
            ta[row][col] = i
            
            if resolve(ta):
                return True
        ta[row][col] = 0
        

def valid(ta, num, pos):
    #checar coluna
    for i in range(len(ta[0])):
        if ta[pos[0]][i] == num and pos[1] != i:
            return False
    
    #checar linha
    for i in range(len(ta)):
        if ta[i][pos[1]] == num and pos[0] !=i:
            return False
        
    #checar matriz
    mat_x = pos[1] // 3
    mat_y = pos[0] // 3
    
    for i in range(mat_y*3, mat_y*3 + 3):
        for j in range(mat_x*3, mat_x*3+3):
            if ta[i][j] == num and (i,j) != pos:
                return False
    
    return True


#funcao para separar tabela
def print_tabela(ta):
    for i in range (len(ta)):
        if i % 3==0 and i !=0:
            print (" - - - - - - - - - - - - - ")
            
        for j in range (len(ta)):
            if j %3==0 and j !=0:
                print (" | ", end="" )
                
            if j==8:
                print(ta[i][j])
            else:
                print(str(ta[i][j]) + " ", end="")

def procura_0(ta):
    for i in range(len(ta)):
        for j in range(len(ta)):
            if ta[i][j]==0:
                return(i,j)
    return None

print_tabela(tabela)
resolve(tabela)
print("_________________________")
print_tabela(tabela)
