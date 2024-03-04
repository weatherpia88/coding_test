#미완성 입니다.

def call_count_one(i,j,board2):
    print(i,j)
    board3 = board2
    if i > 0 and j > 0:
       for i in range(i-1,i+1):
           for j in range(j-1,j+1):
               if board2[int(i)][int(j)] == 'O':
                  board3[int(i)][int(j)] == 'X'  
                   
    #return board3
def solution(board):
    print(board)
    board2= []
    #m == board.length
    #n == board[i].length
    sum = 0
    
    for i in range(0,len(board)):
        board2.append(board[i])
    
    for i in range(0,len(board)):
        for j in range(0,len(board[1])):
            #print(board2[int(i)][int(j)])
            if board2[int(i)][int(j)] == 'O':
                #print(i,j)
                call_count_one(i,j,board2)

    
    
    
    #print(k,k1)    

    #print(len(board),int(sum/len(board)))
    #board2 = [len(board)][int(sum/len(board))]
    #print(board2)    
        
        
        
        
    











solution([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])