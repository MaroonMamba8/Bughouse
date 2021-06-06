import pieces

class Board:
    WIDTH = 8
    HEIGHT = 8

    def __init__(self, positions, pawn_wjustmoved_x, pawn_wjustmoved_y, pawn_bjustmoved_x, pawn_bjustmoved_y):
        self.positions = positions
        self.pawn_wjustmoved_x = pawn_wjustmoved_x
        self.pawn_wjustmoved_y = pawn_wjustmoved_y
        self.pawn_bjustmoved_x = pawn_bjustmoved_x
        self.pawn_bjustmoved_y = pawn_bjustmoved_y

    ## gets the piece of a board's position        
    def get_piece(self,x,y):
        return self.positions[x][y]

    ## performs the move on a board
    def do_move(self, move):
        first_piece = self.positions[move.x1][move.y1]
        first_piece.x = move.x2
        first_piece.y = move.y2
        first_piece.moved = True

        # if the pawn just moved last turn, it should now be False
        ## implement for both colors
        if first_piece.color == "W":
            if self.pawn_wjustmoved_x != -1:
                pawn = self.get_piece(self.pawn_wjustmoved_x,self.pawn_wjustmoved_y)
                pawn.justmoved = False 
                self.pawn_wjustmoved_x = -1
                self.pawn_wjustmoved_y = -1

        if first_piece.color == "B":
            if self.pawn_bjustmoved_x != -1:
                pawn = self.get_piece(self.pawn_bjustmoved_x,self.pawn_bjustmoved_y)
                pawn.justmoved = False 
                self.pawn_bjustmoved_x = -1
                self.pawn_bjustmoved_y = -1

        p = self.positions[move.x2][move.y2]        
        self.positions[move.x1][move.y1] = None
        self.positions[move.x2][move.y2] = first_piece

        ## special pawn cases
        if first_piece.type == "P":
            if move.promotion == 0:
                if (p == None and move.x2 != move.x1):
                    ## en passant case
                    self.positions[move.x2][move.y1] = None
                    if first_piece.color == "W":
                        self.pawn_bjustmoved_x = -1
                        self.pawn_bjustmoved_y = -1
                    else:
                        self.pawn_wjustmoved_x = -1
                        self.pawn_wjustmoved_y = -1
                if abs(move.y2 - move.y1) == 2:
                    ## pawn's first move is two steps
                    first_piece.justmoved = True
                    if first_piece.color == "W":
                        self.pawn_wjustmoved_x = move.x2 
                        self.pawn_wjustmoved_y = move.y2
                    else:
                        self.pawn_bjustmoved_x = move.x2 
                        self.pawn_bjustmoved_y = move.y2
            elif move.promotion == 1:
                n = pieces.Knight(first_piece.color,move.x2,move.y2)
                n.waspromoted = True 
                n.moved = True
                self.positions[move.x2][move.y2] = n
            elif move.promotion == 2:
                b = pieces.Bishop(first_piece.color,move.x2,move.y2)
                b.waspromoted = True 
                b.moved = True
                self.positions[move.x2][move.y2] = b
            elif move.promotion == 3:
                r = pieces.Rook(first_piece.color,move.x2,move.y2)
                r.waspromoted = True 
                r.moved = True
                self.positions[move.x2][move.y2] = r
            else:
                q = pieces.Queen(first_piece.color,move.x2,move.y2)
                q.waspromoted = True 
                q.moved = True
                self.positions[move.x2][move.y2] = q

        ## special king castling cases; move the rook
        if first_piece.type == "K":
            if move.castle == True:
                if move.x2 == move.x1 + 2:
                    r = self.get_piece(move.x1+3,move.y1)
                    r.x = move.x1+1
                    self.positions[move.x1+3][move.y1] = None 
                    self.positions[move.x1+1][move.y1] = r 
                else:
                    r = self.get_piece(move.x1-4,move.y1)
                    r.x = move.x1+1
                    self.positions[move.x1-4][move.y1] = None 
                    self.positions[move.x1-1][move.y1] = r                    

    ## all legal moves without accounting for checks
    def legal_moves(self,color):
        moves = []
        for i in range(Board.WIDTH):
            for j in range(Board.HEIGHT):
                p = self.positions[i][j]
                if (p != None) and (p.color == color):
                    for move in p.possible_moves(self):
                        moves.append(move)
        return moves

    ## the "true" legal moves a color can play, i.e. their king can be safe
    def real_legal_moves(self, color):
        list_moves = []
        legal_moves = self.legal_moves(color)
        for move in legal_moves:
            copy = self.clone_board()
            copy.do_move(move)
            (x,y) = copy.find_king(color)
            if move.castle == False:
                if not copy.in_check(x,y,color):
                    list_moves.append(move)
            else:
                if move.x2 == move.x1 + 2:
                    if not (copy.in_check(x,y,color) or copy.in_check(x+1,y,color) or copy.in_check(x+2,y,color)):
                        list_moves.append(move)
                else:
                    if not (copy.in_check(x,y,color) or copy.in_check(x-1,y,color) or copy.in_check(x-2,y,color)):
                        list_moves.append(move)
        return list_moves

    ## finds the position of a color's king, used as a helper
    def find_king(self,color):
        for i in range(Board.WIDTH):
            for j in range(Board.HEIGHT):
                k = self.positions[i][j]
                if (k != None) and (k.color == color) and (k.type == "K"):
                    return (i,j)
        return None

    ## finds the positions with no pieces, used as a bughouse helper 
    def find_emptys(self):
        empty_list = []
        for i in range(Board.WIDTH):
            for j in range(Board.HEIGHT):
                e = self.positions[i][j]
                if e == None:
                    empty_list.append((i,j))
        return empty_list

    ## a bool to check if the color is currently in check
    def in_check(self,x1,y1,color):
        ## applies only for the king's position (x1,y1)
        if color == "W":
            opponent_color = "B"
        else:
            opponent_color = "W"
        for move in self.legal_moves(opponent_color):
            copy = self.clone_board()
            copy.do_move(move)
            for i in range(Board.WIDTH):
                for j in range(Board.HEIGHT):
                    p = copy.positions[i][j]
                    if (p != None) and (p.x == x1) and (p.y == y1) and (p.color == opponent_color):
                        return True 
        return False

    ## clones the board 
    def clone_board(self):
        new_positions = [[None]*Board.HEIGHT for i in range(Board.WIDTH)]
        for i in range(Board.WIDTH):
            for j in range(Board.HEIGHT):
                p = self.positions[i][j]
                if (p != None):
                    new_positions[i][j] = p.clone()
        return Board(new_positions,self.pawn_wjustmoved_x,self.pawn_wjustmoved_y,self.pawn_bjustmoved_x,self.pawn_bjustmoved_y)

    ## prints the board's diagram
    def to_string(self):
        string = "                               \n"
        for j in range(Board.HEIGHT):
            string += str(Board.HEIGHT - j) + " | "
            for i in range(Board.WIDTH):
                p = self.positions[i][Board.HEIGHT-j-1] 
                if p == None:
                    string += "   "
                else:
                    string += p.to_string() + " "
            string += " | \n"
        string += "    A  B  C  D  E  F  G  H     "
        return string

class Move:

    def __init__(self,x1,y1,x2,y2,castle,promotion):
        ## (x1,y1),(x2,y2) are from and to coordinates
        ## castle is a bool and promotion is a number
        self.x1 = x1
        self.y1 = y1 
        self.x2 = x2 
        self.y2 = y2 
        self.castle = castle 
        self.promotion = promotion

    def __eq__(self,move):
        if move == None:
            return False
        return self.x1 == move.x1 and self.y1 == move.y1 and self.x2 == move.x2 and self.y2 == move.y2 and self.castle == move.castle and self.promotion == move.promotion

    def to_string(self):
        if self.promotion == "1":
            return "PROMOTION (" + str(self.x2) + ", " + str(self.y2) + ") = N"
        if self.promotion == "2":
            return "PROMOTION (" + str(self.x2) + ", " + str(self.y2) + ") = B"
        if self.promotion == "3":
            return "PROMOTION (" + str(self.x2) + ", " + str(self.y2) + ") = R"        
        if self.promotion == "4":
            return "PROMOTION (" + str(self.x2) + ", " + str(self.y2) + ") = Q"
        else:
            if self.castle == True:
                return "CASTLE (" + str(self.x1) + ", " + str(self.y1) + ") -> (" + str(self.x2) + ", " + str(self.y2) + ")"
            else:
                return "(" + str(self.x1) + ", " + str(self.y1) + ") -> (" + str(self.x2) + ", " + str(self.y2) + ")"

def Board_standard_setup():
        positions = [[None]*Board.HEIGHT for i in range(Board.WIDTH)]
        for i in range(Board.WIDTH):
            positions[i][1] = pieces.Pawn("W",i,1)
            positions[i][Board.HEIGHT-2] = pieces.Pawn("B",i,Board.HEIGHT-2)
        
        positions[0][0] = pieces.Rook("W",0,0)
        positions[0][Board.HEIGHT-1] = pieces.Rook("B",0,Board.HEIGHT-1)
        positions[Board.WIDTH-1][0] = pieces.Rook("W",Board.WIDTH-1,0)
        positions[Board.WIDTH-1][Board.HEIGHT-1] = pieces.Rook("B",Board.WIDTH-1,Board.HEIGHT-1)

        positions[1][0] = pieces.Knight("W",1,0)
        positions[1][Board.HEIGHT-1] = pieces.Knight("B",1,Board.HEIGHT-1)
        positions[Board.WIDTH-2][0] = pieces.Knight("W",Board.WIDTH-2,0)
        positions[Board.WIDTH-2][Board.HEIGHT-1] = pieces.Knight("B",Board.WIDTH-2,Board.HEIGHT-1)

        positions[2][0] = pieces.Bishop("W",2,0)
        positions[2][Board.HEIGHT-1] = pieces.Bishop("B",2,Board.HEIGHT-1)
        positions[Board.WIDTH-3][0] = pieces.Bishop("W",Board.WIDTH-3,0)
        positions[Board.WIDTH-3][Board.HEIGHT-1] = pieces.Bishop("B",Board.WIDTH-3,Board.HEIGHT-1)

        positions[3][0] = pieces.Queen("W",3,0)
        positions[3][Board.HEIGHT-1] = pieces.Queen("B",3,Board.HEIGHT-1)
        positions[Board.WIDTH-4][0] = pieces.King("W",Board.WIDTH-4,0)
        positions[Board.WIDTH-4][Board.HEIGHT-1] = pieces.King("B",Board.WIDTH-4,Board.HEIGHT-1)

        return Board(positions,-1,-1,-1,-1)

## Adding piece reserves to the board

class ReserveBoard:

    def __init__(self,board,wreserve,breserve):
        self.board = board 
        self.wreserve = wreserve 
        self.breserve = breserve 
        self.name = "Board"

    ## performs the standard board move or placing piece onto board
    def do_move(self,move):
        typemove = move.typemove 
        if isinstance(typemove,Move):
            self.board.do_move(typemove)
        else:
            p = typemove.piece.clone()
            x = typemove.x 
            y = typemove.y 
            if p.color == "W":
                remove_from_list(p,self.wreserve)
            else:
                remove_from_list(p,self.breserve)
            self.board.positions[x][y] = p
            p.x = x
            p.y = y

    ## retrives captured piece, if any, on a move
    def get_captured_piece(self,move):
        typemove = move.typemove
        if isinstance(typemove,PlacePiece):
            return None 
        else:
            ## en passant case
            first_piece = self.board.get_piece(typemove.x1,typemove.y1)
            captured_piece = self.board.get_piece(typemove.x2,typemove.y2)
            if first_piece.type == "P" and captured_piece == None and typemove.x1 != typemove.x2:
                captured_piece = self.board.get_piece(typemove.x2,typemove.y1)
            return captured_piece

    ## clones board and its reserve 
    def clone_rboard(self):
        b = self.board.clone_board()
        new_wreserve = []
        new_breserve = []
        for piece in self.wreserve:
            p = piece.clone()
            new_wreserve.append(p)
        for piece in self.breserve:
            p = piece.clone()
            new_breserve.append(p)
        return ReserveBoard(b,new_wreserve,new_breserve)

    ## gets legal board moves for a color, excluding checks
    def move_legal_moves(self,color):
        moves_list = []
        candidates = self.board.legal_moves(color)
        for move in candidates:
            moves_list.append(BugMove(self.name,move))
        return moves_list

    ## gets legal piece placing moves for a board and color, excluding checks
    def placepiece_legal_moves(self,color):
        moves_list = []
        if color == "W":
            reserve_pieces = get_distinct_pieces(self.wreserve)
            empty_squares = self.board.find_emptys()
        else:
            reserve_pieces = get_distinct_pieces(self.breserve)
            empty_squares = self.board.find_emptys()
        for piece in reserve_pieces:
            ## pawns cannot go on first or eighth ranks
            if piece.type == "P":
                for space in empty_squares:
                    (x,y) = space 
                    if 0 < y < Board.HEIGHT-1:
                        moves_list.append(BugMove(self.name,PlacePiece(piece,x,y)))
            else:
                for space in empty_squares:
                    (x,y) = space 
                    moves_list.append(BugMove(self.name,PlacePiece(piece,x,y)))
        return moves_list

    ## gets all legal moves for a color, without accounting for checks
    def all_legal_moves(self,color):
        return self.move_legal_moves(color) + self.placepiece_legal_moves(color)

    ## gets all legal moves for a color, accounting for checks
    def real_legal_moves(self,color):
        list_moves = []
        legal_moves = self.all_legal_moves(color)
        for move in legal_moves:
            copy = self.clone_rboard()
            copy.do_move(move)
            (x,y) = copy.board.find_king(color)
            typemove = move.typemove
            if isinstance(typemove,PlacePiece):
                if not copy.in_check(color,x,y):
                    list_moves.append(move)
            else:
                if typemove.castle == False:
                    if not copy.in_check(color,x,y):
                        list_moves.append(move)
                else:
                    if typemove.x2 == typemove.x1 + 2:
                        if not (copy.in_check(color,x,y) or copy.in_check(color,x+1,y) or copy.in_check(color,x+2,y)):
                            list_moves.append(move)
                    else:
                        if not (copy.in_check(color,x,y) or copy.in_check(color,x-1,y) or copy.in_check(color,x-2,y)):
                            list_moves.append(move)
        return list_moves
    
    ## checks if a certain square (x,y) is attacked on the board
    def in_check(self,color,x,y):
        if color == "W":
            opponent_color = "B"
        else:
            opponent_color = "W"
        for move in self.all_legal_moves(opponent_color):
            copy = self.clone_rboard()
            copy.do_move(move)
            for i in range(Board.WIDTH):
                for j in range(Board.HEIGHT):
                    p = copy.board.positions[i][j]
                    if (p != None) and (p.x == x) and (p.y == y) and (p.color == opponent_color):
                        return True 
        return False

## Now extending the game to two boards

class DoubleBoard:

    def __init__(self, rboard1, rboard2):
        self.rboard1 = rboard1 
        self.rboard2 = rboard2

    ## performs the bugmove and if a piece is captured, puts it in the right reserve
    def do_move(self,move):
        rboardname = move.rboardname
        if rboardname == "Board1":
            board_ = self.rboard1
        else:
            board_ = self.rboard2
        captured_piece = board_.get_captured_piece(move)
        board_.do_move(move)
        if captured_piece != None:
            if captured_piece.type == "P":
                if captured_piece.color == "W":
                    p = pieces.Pawn("W",Board.WIDTH,Board.HEIGHT)
                    if rboardname == "Board1":
                        self.rboard2.wreserve.append(p)
                    else:
                        self.rboard1.wreserve.append(p)
                else:
                    p = pieces.Pawn("B",Board.WIDTH,Board.HEIGHT)
                    if rboardname == "Board1":
                        self.rboard2.breserve.append(p)
                    else:
                        self.rboard1.breserve.append(p)                        
            ## if the piece was promoted and captured, it's a pawn
            elif captured_piece.waspromoted:
                if captured_piece.color == "W":
                    p = pieces.Pawn("W",Board.WIDTH,Board.HEIGHT)
                    if rboardname == "Board1":
                        self.rboard2.wreserve.append(p)
                    else:
                        self.rboard1.wreserve.append(p)
                else:
                    p = pieces.Pawn("B",Board.WIDTH,Board.HEIGHT)
                    if rboardname == "Board1":
                        self.rboard2.breserve.append(p)
                    else:
                        self.rboard1.breserve.append(p)                        
            else:
                if captured_piece.type == "N" and captured_piece.color == "W":
                    p = pieces.Knight("W",Board.WIDTH,Board.HEIGHT)
                    if rboardname == "Board1":
                        self.rboard2.wreserve.append(p)
                    else:
                        self.rboard1.wreserve.append(p)
                if captured_piece.type == "B" and captured_piece.color == "W":
                    p = pieces.Bishop("W",Board.WIDTH,Board.HEIGHT)
                    if rboardname == "Board1":
                        self.rboard2.wreserve.append(p)
                    else:
                        self.rboard1.wreserve.append(p)
                if captured_piece.type == "R" and captured_piece.color == "W":
                    p = pieces.Rook("W",Board.WIDTH,Board.HEIGHT)
                    if rboardname == "Board1":
                        self.rboard2.wreserve.append(p)
                    else:
                        self.rboard1.wreserve.append(p)
                if captured_piece.type == "Q" and captured_piece.color == "W":
                    p = pieces.Queen("W",Board.WIDTH,Board.HEIGHT)
                    if rboardname == "Board1":
                        self.rboard2.wreserve.append(p)
                    else:
                        self.rboard1.wreserve.append(p)
                if captured_piece.type == "N" and captured_piece.color == "B":
                    p = pieces.Knight("B",Board.WIDTH,Board.HEIGHT)
                    if rboardname == "Board1":
                        self.rboard2.breserve.append(p)
                    else:
                        self.rboard1.breserve.append(p)
                if captured_piece.type == "B" and captured_piece.color == "B":
                    p = pieces.Bishop("B",Board.WIDTH,Board.HEIGHT)
                    if rboardname == "Board1":
                        self.rboard2.breserve.append(p)
                    else:
                        self.rboard1.breserve.append(p)
                if captured_piece.type == "R" and captured_piece.color == "B":
                    p = pieces.Rook("B",Board.WIDTH,Board.HEIGHT)
                    if rboardname == "Board1":
                        self.rboard2.breserve.append(p)
                    else:
                        self.rboard1.breserve.append(p)
                if captured_piece.type == "Q" and captured_piece.color == "B":
                    p = pieces.Queen("B",Board.WIDTH,Board.HEIGHT)
                    if rboardname == "Board1":
                        self.rboard2.breserve.append(p)
                    else:
                        self.rboard1.breserve.append(p)

    ## displays both boards and their reserves
    def to_string(self):
        (w1,w2) = format_reserve(self.rboard1.wreserve)
        (b1,b2) = format_reserve(self.rboard2.breserve)
        (b3,b4) = format_reserve(self.rboard1.breserve)
        (w3,w4) = format_reserve(self.rboard2.wreserve)
        string = ' ' * 12 + "Board 1" + ' ' * 25 + "Board 2" + ' ' * 12 + "\n"
        string += ' ' * 63 + "\n"
        string += w1 + b1 + "\n" + w2 + b2 + "\n"
        string += ' ' * 63 + "\n"
        for j in range(Board.HEIGHT):
            string += str(Board.HEIGHT - j) + " | "
            for i in range(Board.WIDTH):
                p = self.rboard1.board.positions[Board.WIDTH-i-1][j] 
                if p == None:
                    string += "   "
                else:
                    string += p.to_string() + " "
            string += " | "
            string += str(Board.HEIGHT - j) + " | "
            for i in range(Board.WIDTH):
                p = self.rboard2.board.positions[i][Board.HEIGHT-j-1]
                if p == None:
                    string += "   "
                else:
                    string += p.to_string() + " "
            string += " | \n"
        string += "    A  B  C  D  E  F  G  H         A  B  C  D  E  F  G  H     \n"
        string += ' ' * 63 + "\n"
        string += b3 + w3 + "\n" + b4 + w4
        return string

## removes a piece from a reserve
def remove_from_list(item,reserve):
    for j in reserve:
        if item == j:
            reserve.remove(j)
            break

## gets a list of DISTINCT pieces in a reserve
def get_distinct_pieces(reserve):
    if len(reserve) == 0:
        return []
    color = reserve[0].color
    pieces_list = []
    if color == "W":
        candidates = [pieces.Pawn("W",Board.WIDTH,Board.HEIGHT),pieces.Knight("W",Board.WIDTH,Board.HEIGHT),pieces.Bishop("W",Board.WIDTH,Board.HEIGHT),
        pieces.Rook("W",Board.WIDTH,Board.HEIGHT),pieces.Queen("W",Board.WIDTH,Board.HEIGHT)]
    else:
        candidates = [pieces.Pawn("B",Board.WIDTH,Board.HEIGHT),pieces.Knight("B",Board.WIDTH,Board.HEIGHT),pieces.Bishop("B",Board.WIDTH,Board.HEIGHT),
        pieces.Rook("B",Board.WIDTH,Board.HEIGHT),pieces.Queen("B",Board.WIDTH,Board.HEIGHT)]
    for candidate in candidates:
        for piece in reserve:
            if candidate == piece:
                pieces_list.append(candidate)
                break 
    return pieces_list

## format reserves string
def format_reserve(reserve):
    string1 = "R | "
    string2 = "R | "
    if len(reserve) <= Board.WIDTH:
        for i in range(len(reserve)):
            string1 += reserve[i].to_string() + " "
        output1 = string1 + ' ' * (31-len(string1))
        return (output1,' '* (31-len(string1)))
    else:
        for i in range(Board.WIDTH):
            string1 = reserve[i].to_string() + " "
        output1 = string1 + ' ' * (31-len(string1))
        for i in range(Board.WIDTH,len(reserve)):
            string2 += reserve[i].to_string() + " "
        output2 = string2 + ' ' * (31-len(string2))
        return (output1,output2)

class PlacePiece:

    def __init__(self, piece, x, y):
        self.piece = piece 
        self.x = x
        self.y = y

    def __eq__(self,move):
        if move == None:
            return False
        return self.piece == move.piece and self.x == move.x and self.y == move.y

    def to_string(self):
        return self.piece.type + "@" + "(" + str(self.x) + str(self.y) + ")"

class BugMove:

    def __init__(self, rboardname, typemove):
        self.rboardname = rboardname
        self.typemove = typemove 

    def __eq__(self,move):
        if move == None:
            return False
        if isinstance(self.typemove,Move) != isinstance(move.typemove,Move):
            return False
        return self.rboardname == move.rboardname and self.typemove == move.typemove

    def to_string(self):
        return self.rboardname + ": " + self.typemove.to_string()

def ReserveBoard_standard_setup():
    board = Board_standard_setup()
    return ReserveBoard(board,[],[])

def DoubleBoard_standard_setup():
    rboard1 = ReserveBoard_standard_setup()
    rboard1.name = "Board1"
    rboard2 = ReserveBoard_standard_setup()
    rboard2.name = "Board2"
    return DoubleBoard(rboard1,rboard2)