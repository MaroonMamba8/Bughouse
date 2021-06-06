import board

class Piece(object):

    def __init__(self, color, type, x, y):
        self.color = color
        self.type = type
        self.x = x
        self.y = y

    def to_string(self):
        return self.color + self.type

    def __eq__(self,move):
        if move == None:
            return False
        return self.color == move.color and self.type == move.type and self.x == move.x and self.y == move.y

class Pawn(Piece):
    TYPE = "P"
    VALUE = 1

    def __init__(self,color,x,y):
        super(Pawn, self).__init__(color,self.TYPE,x,y)
        self.moved = False
        self.justmoved = False
        self.value = Pawn.VALUE

    def possible_moves(self,board_):
        moves = []
        if self.color == "W":
            front1 = board_.get_piece(self.x,self.y+1)
            if front1 == None:
                if self.y == 1:
                    moves.append(board.Move(self.x,self.y,self.x,self.y+1,False,0))
                    front2 = board_.get_piece(self.x,self.y+2)
                    if front2 == None:
                        moves.append(board.Move(self.x,self.y,self.x,self.y+2,False,0))
                elif self.y == 6:
                    moves.append(board.Move(self.x,self.y,self.x,self.y+1,False,1))
                    moves.append(board.Move(self.x,self.y,self.x,self.y+1,False,2))
                    moves.append(board.Move(self.x,self.y,self.x,self.y+1,False,3))
                    moves.append(board.Move(self.x,self.y,self.x,self.y+1,False,4))
                else:
                    moves.append(board.Move(self.x,self.y,self.x,self.y+1,False,0))
            if self.x >= 1:
                side1 = board_.get_piece(self.x-1,self.y+1)
                if side1 != None and side1.color != self.color:
                    if self.y == 6:
                        moves.append(board.Move(self.x,self.y,self.x-1,self.y+1,False,1))
                        moves.append(board.Move(self.x,self.y,self.x-1,self.y+1,False,2))
                        moves.append(board.Move(self.x,self.y,self.x-1,self.y+1,False,3))
                        moves.append(board.Move(self.x,self.y,self.x-1,self.y+1,False,4))
                    else:
                        moves.append(board.Move(self.x,self.y,self.x-1,self.y+1,False,0))
                elif side1 == None and self.y == 4:
                    left1 = board_.get_piece(self.x-1,self.y)
                    if left1 != None and left1.type == "P" and left1.justmoved:
                        moves.append(board.Move(self.x,self.y,self.x-1,self.y+1,False,0))
            if self.x < board_.WIDTH - 1:
                side1 = board_.get_piece(self.x+1,self.y+1)
                if side1 != None and side1.color != self.color:
                    if self.y == 6:
                        moves.append(board.Move(self.x,self.y,self.x+1,self.y+1,False,1))
                        moves.append(board.Move(self.x,self.y,self.x+1,self.y+1,False,2))
                        moves.append(board.Move(self.x,self.y,self.x+1,self.y+1,False,3))
                        moves.append(board.Move(self.x,self.y,self.x+1,self.y+1,False,4))
                    else:
                        moves.append(board.Move(self.x,self.y,self.x+1,self.y+1,False,0))
                elif side1 == None and self.y == 4:
                    left1 = board_.get_piece(self.x+1,self.y)
                    if left1 != None and left1.type == "P" and left1.justmoved:
                        moves.append(board.Move(self.x,self.y,self.x+1,self.y+1,False,0))
        else:
            front1 = board_.get_piece(self.x,self.y-1)
            if front1 == None:
                if self.y == 6:
                    moves.append(board.Move(self.x,self.y,self.x,self.y-1,False,0))
                    front2 = board_.get_piece(self.x,self.y-2)
                    if front2 == None:
                        moves.append(board.Move(self.x,self.y,self.x,self.y-2,False,0))
                elif self.y == 1:
                    moves.append(board.Move(self.x,self.y,self.x,self.y-1,False,1))
                    moves.append(board.Move(self.x,self.y,self.x,self.y-1,False,2))
                    moves.append(board.Move(self.x,self.y,self.x,self.y-1,False,3))
                    moves.append(board.Move(self.x,self.y,self.x,self.y-1,False,4))
                else:
                    moves.append(board.Move(self.x,self.y,self.x,self.y-1,False,0))
            if self.x >= 1:
                side1 = board_.get_piece(self.x-1,self.y-1)
                if side1 != None and side1.color != self.color:
                    if self.y == 1:
                        moves.append(board.Move(self.x,self.y,self.x-1,self.y-1,False,1))
                        moves.append(board.Move(self.x,self.y,self.x-1,self.y-1,False,2))
                        moves.append(board.Move(self.x,self.y,self.x-1,self.y-1,False,3))
                        moves.append(board.Move(self.x,self.y,self.x-1,self.y-1,False,4))
                    else:
                        moves.append(board.Move(self.x,self.y,self.x-1,self.y-1,False,0))
                elif side1 == None and self.y == 3:
                    left1 = board_.get_piece(self.x-1,self.y)
                    if left1 != None and left1.type == "P" and left1.justmoved:
                        moves.append(board.Move(self.x,self.y,self.x-1,self.y-1,False,0))
            if self.x < board_.WIDTH - 1:
                side1 = board_.get_piece(self.x+1,self.y-1)
                if side1 != None and side1.color != self.color:
                    if self.y == 1:
                        moves.append(board.Move(self.x,self.y,self.x+1,self.y-1,False,1))
                        moves.append(board.Move(self.x,self.y,self.x+1,self.y-1,False,2))
                        moves.append(board.Move(self.x,self.y,self.x+1,self.y-1,False,3))
                        moves.append(board.Move(self.x,self.y,self.x+1,self.y-1,False,4))
                    else:
                        moves.append(board.Move(self.x,self.y,self.x+1,self.y-1,False,0))
                elif side1 == None and self.y == 3:
                    left1 = board_.get_piece(self.x+1,self.y)
                    if left1 != None and left1.type == "P" and left1.justmoved:
                        moves.append(board.Move(self.x,self.y,self.x+1,self.y-1,False,0))
        return moves

    def clone(self):
        p = Pawn(self.color,self.x,self.y) 
        p.moved = self.moved
        p.justmoved = self.justmoved 
        return p

class Knight(Piece):
    TYPE = "N"
    VALUE = 3

    def __init__(self,color,x,y):
        super(Knight, self).__init__(color,self.TYPE,x,y)
        self.moved = False
        self.value = Knight.VALUE
        self.waspromoted = False

    def possible_moves(self,board_):
        moves = []
        candidates = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
        for i in range(len(candidates)):
            if 0 <= self.x + candidates[i][0] < board_.WIDTH and 0 <= self.y + candidates[i][1] < board_.HEIGHT:
                p = board_.get_piece(self.x+candidates[i][0],self.y+candidates[i][1])
                if p == None or p.color != self.color:
                    moves.append(board.Move(self.x,self.y,self.x+candidates[i][0],self.y+candidates[i][1],False,0))
        return moves

    def clone(self):
        n = Knight(self.color,self.x,self.y)
        n.moved = self.moved 
        n.waspromoted = self.waspromoted 
        return n

class Bishop(Piece):
    TYPE = "B"
    VALUE = 3.15

    def __init__(self,color,x,y):
        super(Bishop, self).__init__(color,self.TYPE,x,y)
        self.moved = False
        self.value = Bishop.VALUE
        self.waspromoted = False

    def possible_moves(self,board_):
        moves = []
        for i in range(1,min(board_.WIDTH-self.x,board_.HEIGHT-self.y)):
            p = board_.get_piece(self.x+i,self.y+i)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x+i,self.y+i,False,0))
        for i in range(1,min(self.x+1,self.y+1)):
            p = board_.get_piece(self.x-i,self.y-i)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x-i,self.y-i,False,0))
        for i in range(1,min(self.x+1,board_.HEIGHT-self.y)):
            p = board_.get_piece(self.x-i,self.y+i)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x-i,self.y+i,False,0))
        for i in range(1,min(board_.WIDTH-self.x,self.y+1)):
            p = board_.get_piece(self.x+i,self.y-i)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x+i,self.y-i,False,0))
        return moves 

    def clone(self):
        b = Bishop(self.color,self.x,self.y)
        b.moved = self.moved 
        b.waspromoted = self.waspromoted 
        return b

class Rook(Piece):
    TYPE = "R"
    VALUE = 5

    def __init__(self,color,x,y):
        super(Rook, self).__init__(color,self.TYPE,x,y)
        self.moved = False
        self.value = Rook.VALUE
        self.waspromoted = False

    def possible_moves(self,board_):
        moves = []
        for i in range(1,board_.WIDTH-self.x):
            p = board_.get_piece(self.x+i,self.y)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x+i,self.y,False,0))
        for i in range(1,self.x+1):
            p = board_.get_piece(self.x-i,self.y)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x-i,self.y,False,0))
        for i in range(1,board_.HEIGHT-self.y):
            p = board_.get_piece(self.x,self.y+i)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x,self.y+i,False,0))
        for i in range(1,self.y+1):
            p = board_.get_piece(self.x,self.y-i)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x,self.y-i,False,0))
        return moves

    def clone(self):
        r = Rook(self.color,self.x,self.y) 
        r.moved = self.moved 
        r.waspromoted = self.waspromoted 
        return r

class Queen(Piece):
    TYPE = "Q"
    VALUE = 9

    def __init__(self,color,x,y):
        super(Queen, self).__init__(color,self.TYPE,x,y)
        self.moved = False
        self.value = Queen.VALUE
        self.waspromoted = False

    def possible_moves(self,board_):
        moves = []
        for i in range(1,min(board_.WIDTH-self.x,board_.HEIGHT-self.y)):
            p = board_.get_piece(self.x+i,self.y+i)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x+i,self.y+i,False,0))
        for i in range(1,min(self.x+1,self.y+1)):
            p = board_.get_piece(self.x-i,self.y-i)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x-i,self.y-i,False,0))
        for i in range(1,min(self.x+1,board_.HEIGHT-self.y)):
            p = board_.get_piece(self.x-i,self.y+i)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x-i,self.y+i,False,0))
        for i in range(1,min(board_.WIDTH-self.x,self.y+1)):
            p = board_.get_piece(self.x+i,self.y-i)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x+i,self.y-i,False,0))
        for i in range(1,board_.WIDTH-self.x):
            p = board_.get_piece(self.x+i,self.y)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x+i,self.y,False,0))
        for i in range(1,self.x+1):
            p = board_.get_piece(self.x-i,self.y)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x-i,self.y,False,0))
        for i in range(1,board_.HEIGHT-self.y):
            p = board_.get_piece(self.x,self.y+i)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x,self.y+i,False,0))
        for i in range(1,self.y+1):
            p = board_.get_piece(self.x,self.y-i)
            if p != None and p.color == self.color:
                break
            elif p != None and p.color != self.color:
                moves.append(board.Move(self.x,self.y,p.x,p.y,False,0))
                break
            else:
                moves.append(board.Move(self.x,self.y,self.x,self.y-i,False,0))       
        return moves

    def clone(self):
        q = Queen(self.color,self.x,self.y)
        q.moved = self.moved 
        q.waspromoted = self.waspromoted 
        return q

class King(Piece):
    TYPE = "K"
    VALUE = 1000

    def __init__(self,color,x,y):
        super(King, self).__init__(color,self.TYPE,x,y)
        self.moved = False
        self.value = King.VALUE

    def castle_right(self,board_):
        if self.moved:
            return False
        r = board_.get_piece(self.x+3,self.y)
        if r == None:
            return False
        if r.type != "R" or r.color != self.color or r.moved:
            return False 
        piece1 = board_.get_piece(self.x+1,self.y)
        piece2 = board_.get_piece(self.x+2,self.y)
        if piece1 != None or piece2 != None:
            return False 
        return True

    def castle_left(self,board_):
        if self.moved:
            return False
        r = board_.get_piece(self.x-4,self.y)
        if r == None:
            return False
        if r.type != "R" or r.color != self.color or r.moved:
            return False 
        piece1 = board_.get_piece(self.x-1,self.y)
        piece2 = board_.get_piece(self.x-2,self.y)
        piece3 = board_.get_piece(self.x-3,self.y)
        if piece1 != None or piece2 != None or piece3 != None:
            return False 
        return True

    def possible_moves(self,board_):
        moves = []
        candidates = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
        for i in range(len(candidates)):
            if 0 <= self.x + candidates[i][0] < board_.WIDTH and 0 <= self.y + candidates[i][1] < board_.HEIGHT:
                p = board_.get_piece(self.x+candidates[i][0],self.y+candidates[i][1])
                if p == None or p.color != self.color:
                    moves.append(board.Move(self.x,self.y,self.x+candidates[i][0],self.y+candidates[i][1],False,0))
        if self.castle_right(board_):
            moves.append(board.Move(self.x,self.y,self.x+2,self.y,True,0))
        if self.castle_left(board_):
            moves.append(board.Move(self.x,self.y,self.x-2,self.y,True,0))
        return moves

    def clone(self):
        k = King(self.color,self.x,self.y)
        k.moved = self.moved 
        return k