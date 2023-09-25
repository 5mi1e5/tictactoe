row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']
board= [row1,row2,row3]

def prin_brd():
    print('|'.join(row1))
    print('|'.join(row2))
    print('|'.join(row3))

def enter_val_X(row,ind):
    row-=1
    ind -=1
    board[row][ind]="X"
    prin_brd()

def enter_val_O(row,ind):
    row-=1
    ind -=1
    board[row][ind]="O"
    prin_brd()

count=0
while count in range(9):
    choice= input("X or O??:")
    a=int(input("enter row:"))
    b=int(input("enter the index of the row:"))

    if choice=="x":
        enter_val_X(a,b)
    elif choice=="o":
        enter_val_O(a,b)
    else:
        print("son of a bit5rotgkg!?!?!?")
    count +=1
