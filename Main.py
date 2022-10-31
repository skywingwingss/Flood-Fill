from typing import List



board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]



def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """
    # Implement your code here
    #transform the input string list into array list
    board=[]
    for i in range(len(input_board)):
        str=[]
        for j in range(len(input_board[i])):
            str.append(input_board[i][j])
        board.append(str)

    #get array list shape
    maxY=len(board[0])-1
    maxX=len(board)-1
    #store the unexplored points
    Coordinate = []
    Coordinate.extend([(x,y)])

    while True:
        #if there is still some points unexplored
        if len(Coordinate)>0:
            x,y=Coordinate[0]
            del Coordinate[0]
            if x>=0 and y>=0 and x<=maxX and y<=maxY:
                if board[x][y]==old:
                    #update the point value and coordinate list
                    board[x][y]=new
                    Coordinate.extend([(x,y+1),(x+1,y),(x-1,y),(x,y-1)])
        else:
            break
    #concatenate the array list into string list and output
    Ans=[]
    for i in range(len(board)):
        Ans.append(''.join(board[i]))


    return Ans





modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....