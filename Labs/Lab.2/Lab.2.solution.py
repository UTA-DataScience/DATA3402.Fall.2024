#!/usr/bin/env python
# coding: utf-8

# ## Lab 2- Tic Tac Toe

# #### Exercise 1: Wrie a function that creates an n by n matrix(of list of lists) which will represent the state of a Tic Tac Toe game. Let 0, 1, and 2, represent empty, "X", and "O", respectively. 

# In[1]:


player_1 = 'X'
player_2 = 'O'
empty = 0 


# In[2]:


def create_matrix(n):
    matrix = list()
    for i in range(n):
        row = list()
        for j in range(n):
            row.append(empty)
    
                
            
        matrix.append(row)
    return matrix


# In[3]:


tic_tac_board = create_matrix(3)


# In[4]:


tic_tac_board
# not printing correctly 


# #### Exercise 2: Write a function that takes 2 integers n and m as input and draws a n by m game board. 

# In[5]:


def create_matrix_1(n,m):
    matrix_2 =[[empty]*n for i in range(n)] 
    return matrix_2


n = int(input('number = '))
m = int(input('number = '))
result = create_matrix_1(n,m)
print(result)


# #### Exercise 3: Modify exercise 2, so that it takes a matrix of the form from exercise 1 and draws a tic-tac-toe board with "X"s and "O"s. 

# In[6]:


# Modification of exercise 2
def create_matrix(n):
    matrix = list()
    for i in range(n):
        row = list()
        for j in range(n):
            row.append(empty)
            
        matrix.append(row)
    return matrix


# In[7]:


tic_tac_board_1 = create_matrix(3)


# In[8]:


tic_tac_board_1


# In[9]:


def create_matrix_2(n):
    # making of empty board
    n = int(input('number = '))
    matrix = [[empty]*n for i in range(n)] 
    
    # making of even columns
    for i in range(0,n,2):
        matrix[1][i]=player_1
        matrix[-1][i]=player_2
        matrix[1][i]=player_2
        matrix[0][i]=player_1
    
    # making of odd columns
    for i in range(1,n,2):
        matrix[0][i]=player_2
        matrix[2][i]=player_1
        matrix[1][1]= player_1
       
        
    return matrix


# In[10]:


matrix_2 = create_matrix_2(3)


# In[11]:


matrix_2


# #### Exercise 4: Write a function that takes a n by n matrix representing a tic-tac-toe game, and returns -1, 0, 1, or 2 indicating the game is incomplete, the game is a draw, player 1 has won, or player 2 has won, respectivley. 

# In[12]:


#Labels(what they are supposed to represent) 

incomplete_game = -1
draw = 0 
player_1_won = 1
player_2_won = 2


# In[13]:


def create_matrix_2(n):
    # making of empty board
    matrix = [[empty]*n for i in range(n)]
    
    # making of even columns
    for i in range(0,n,2):
        matrix[1][i]=player_1
        matrix[-1][i]=player_2
        matrix[1][i]=player_2
        matrix[0][i]=player_1
    
    # making of odd columns
    for i in range(1,n,2):
        matrix[0][i]=player_1
        matrix[2][i]=player_1
        matrix[1][1]= player_1
        
    # Won, draw, incomplete
    if player_2*n in ():
        print(player_2_won)
    elif player_1*n in ():
        print(player_1_won)
    elif player_2*n or player_1*n not in ():
        print(draw)
    else:
        print(incomplete_game)
        
            
       
        
    return matrix

# function that takes an n by n matrix  now we need the return 


# In[14]:


matrix_5 = create_matrix_2(3)
matrix_5


# In[15]:


# first code for winning_conditions 
def winning_condition(matrix, player):
    m = len(matrix)
    for i in range(n):
        if all (matrix[i][j] == player for j in range(n)):
            return True
        if all (matrix[j][i] == player for j in range(n)):
            return True
        if all (matrix[i][i] == player for i in range(n))  or all (matrix[i][n-i-1] == player for i in range(n)):
            return True
        return False


# In[16]:


# Second Code for winning conditions
def create_matrix_2(n):
    n = int(input('number = '))
    # making of empty board
    matrix = [[empty]*n for i in range(n)]
    
    # making of even columns
    for i in range(0,n,2):
        matrix[1][i]=player_1
        matrix[-1][i]=empty
        matrix[1][i]=player_2
        matrix[0][i]=empty
        
    # making of odd columns
    for i in range(1,n,2):
        matrix[0][i]=player_2
        matrix[2][i]=empty
        matrix[1][1]=player_1 
        
    # Won, draw, incomplete
    if winning_condition(matrix, player_1):
        print(player_1_won)
    elif winning_condition(matrix,player_2):
        print(player_2_won)
    elif all(matrix[i][j] != empty for j in range(n)) or all(matrix[j][i] != empty for j in range(n)):
        print(draw)
    elif (matrix[i][j] == empty for j in range(n)) or (matrix[j][i] == empty for j in range(n)):
        print(incomplete_game)
        

        

   
        
            
       
        
    return matrix


# In[17]:


matrix_6 = create_matrix_2(3)
matrix_6


# In[18]:


winning_condition(matrix_6,player_1)


# In[19]:


winning_condition(matrix_6, player_2)


# #### Exercise 5: Write a function that takes a game board, player number, and (x,y) coordinates and places "X" or "O" in the correct location of the game board. Make sure that you only allow filling previously empty locations. Return True or False to indicate successful placement of "X" or "O". 

# In[21]:


player_1 = 1
player_2 = 2
empty = 0 


# In[25]:


player_1_piece = "X"
player_2_piece = "O"
empty_space = ""


# In[23]:


def create_matrix(n):
    matrix = list()
    for i in range(n):
        row = list()
        for j in range(n):
            row.append(empty)
            
        matrix.append(row)
    return matrix


# In[40]:


def placing(matrix, player_number, coordinates):
    # checking board dimensions
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return False 
    # Is cell empty:
    if matrix[x][y] is not empty: 
        return False
    
    # Placing the X's and O's  
    if player == player_1_piece:
        matrix[x][y] = "X"
    elif player == player_2_peice:
        matrix[x][y] = "O"
    else:
        empty
        


# #### Exercise 6: Modify Exercise 4 to show column and row labels so that players can specify location using "A2" or "C1". 

# In[20]:


def create_matrix(n):
    matrix = list()
    for i in range(n):
        row = list()
        for j in range(n):
            row.append(empty)
            
        matrix.append(row)
    return matrix


# In[21]:


tic_tac_board = create_matrix(3)
tic_tac_board


# In[22]:


def space_character(player):
    if player==player_1:
        return player_1_piece
    if player==player_2:
        return player_2_piece
    else:
        return empty_space
    


# In[26]:


# Testing space_character:
space_character = { player_1:player_1_piece,
                    empty:empty_space,
                    player_2:player_2_piece}
space_character


# In[27]:


n = 3


# In[45]:


def draw_board(matrix):
    for i in range(n):
        for j in range(n):
            print(space_character[matrix[i][j]],end=" ")
        print()
            


# In[46]:


# Testing draw_board(matrix)
# I want to see the 0 in the empty space where the X's and O's are 
# supposed to be.
draw_board(tic_tac_board)


# In[30]:


row_names = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
row_map = dict(zip(row_names, range(n)))


# In[31]:


row_map


# In[32]:


column_names = list(map(str,range(1, n + 1)))
column_map = dict(zip(column_names, range(n)))


# In[33]:


column_map


# In[36]:


n = 3


# In[37]:


def create_matrix_8(matrix):
    print(" ", end=" ")
    for j in range(n):
        print(column_names[j],end=" ")
    print()
    
    for i in range(n):
        print(row_names[i],end=" ")
        for j in range(n):
            print(space_character[matrix[i][j]], end=" ")
        print()


# In[38]:


create_matrix_8(tic_tac_board)
# Fix the space between the letters. How?? 


# In[41]:


def coordinates(length_string):
    if not isinstance(length_string,str):
        print_message("Bad Input. Location must be string.")
        return False 
    
    if len(length_string) !=2:
        print_message("Bad Input. Location must be 2 characters.")
        return False 
    
    row=length_string[0].upper()
    col=length_string[1].upper()
    
    if not row in row_names:
        print_message("Bad Row.")
        return False
    if not col in column_names:
        print_message("Bad Column.")


# In[42]:


coordinates("A3")


# In[58]:


def create_matrix_2(n):
    # making of empty board
    n = int(input('number = '))
    matrix = [[empty]*n for i in range(n)] 
    
    # making of even columns
    for i in range(0,n,2):
        matrix[1][i]=player_1
        matrix[-1][i]=player_2
        matrix[1][i]=player_2
        matrix[0][i]=player_1
    
    # making of odd columns
    for i in range(1,n,2):
        matrix[0][i]=player_2
        matrix[2][i]=player_1
        matrix[1][1]= player_1
       
        
    return matrix


# In[43]:


create_matrix_8(create_matrix_2(3))


# #### Exericise 7: Write a function that takes a board, player number, and location specified as in exercise 6 and then calls exercise 5 to correctly modify the board. 

# In[52]:


def place_marker(board, player = player, x = row, y = col):
    
    
    


# #### Exercise 8: Write a function called with a board and player number, takes input from the player using python's input, and modifies the board using your fucntion form exercise 7. Note that you should keep asking for input until you have gotten a valid input that results in a valid move. 

# In[53]:


def input_function(board,player):
    while True:
        print(f"Current player: {'X' if player == 1 else 'O'}")
        display_matrix(create_matrix_2(n))
        row, col = get_player_input()

        success = place_marker(board, player = player, x = row, y = col)
        if success:
            print(f"Successfully placed {'X' if player == 1 else 'O'} at ({row}, {col}).")
            break
        else:
            print("Invalid move! Try again.")


# #### Exercise 9: Use all of the previous exercises to implement a full tic-tac-toe game, where an appropriate board is drawn, w players are repeatedly asked for a location coordinates of where they wish to place a mark, and the game status is checked until a player wins or a draaw occurs. 

# In[ ]:





# In[ ]:





# #### Exercise 10: Test that you game works for 5x5 Tic Tac Toe. 

# In[ ]:





# In[ ]:





# In[ ]:





# #### Exercise 11: (Advanced / Challenge) Develop a version of the game where one player is the computer. Note that you don't need to do an extensive search for the best move. You can have the computer simply protect against loosing and otherwise try to win wiht straight or diagonal patterns. 

# In[ ]:




