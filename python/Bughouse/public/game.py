import board,pieces

def get_move(dboard,color1,color2):
    print("Board 1: " + color1 + " To Move")
    print("Board 2: " + color2 + " To Move")
    print("If 1 or 2 is the board number")
    print("Format Normal Move: 1 M [Initial Square]-[Final Square]")
    print("Example Normal Move: 1 M e2-e4")
    print("Format Promotion: 1 P [Final Square]=[Piece]")
    print("Example Promotion: 1 P a7-b8=Q")
    print("Format Castle: 1 C K or 2 C Q")
    print("Format Placement: 1 L P/N/B/R/Q @c4")
    string = input("Your Move: ")
    string = string.replace(" ","")
    print(string)

    try:
        if string[0] == "1":
            board_ = dboard.rboard1
            color = color1
        elif string[0] == "2":
            board_ = dboard.rboard2
            color = color2
        else:
            print(string[0])
            print("What's your board number?")
            return get_move(dboard,color1,color2)
        if string[1] == "M":
            x1 = letter_to_digit(string[2])
            y1 = int(string[3])
            x2 = letter_to_digit(string[5])
            y2 = int(string[6])
            return board.BugMove(board_.name,board.Move(x1,y1-1,x2,y2-1,False,0))
        if string[1] == "P":
            x1 = letter_to_digit(string[2])
            y1 = int(string[3])
            x2 = letter_to_digit(string[5])
            y2 = int(string[6])
            p = string[8]
            if y2 == board.Board.HEIGHT and color == "W":
                if p == "N":
                    return board.BugMove(board_.name,board.Move(x1,y2-2,x2,y2-1,False,1))
                if p == "B":
                    return board.BugMove(board_.name,board.Move(x1,y2-2,x2,y2-1,False,2))
                if p == "R":
                    return board.BugMove(board_.name,board.Move(x1,y2-2,x2,y2-1,False,3))
                if p == "Q":
                    return board.BugMove(board_.name,board.Move(x1,y2-2,x2,y2-1,False,4))
                else:
                    print("Invalid promotion format.")
                    return get_move(dboard,color1,color2)       
            if y2 == 1 and color == "B":
                if p == "N":
                    return board.BugMove(board_.name,board.Move(x1,y2,x2,y2-1,False,1))
                if p == "B":
                    return board.BugMove(board_.name,board.Move(x1,y2,x2,y2-1,False,2))
                if p == "R":
                    return board.BugMove(board_.name,board.Move(x1,y2,x2,y2-1,False,3))
                if p == "Q":
                    return board.BugMove(board_.name,board.Move(x1,y2,x2,y2-1,False,4))
                else:
                    print("Invalid promotion format.")
                    return get_move(dboard,color1,color2)
            else:
                print("Invalid promotion format.")
                return get_move(dboard,color1,color2)
        if string[1] == "C":
            p = string[2]
            if p == "K":
                if color == "W":
                    return board.BugMove(board_.name,board.Move(4,0,6,0,True,0))
                else:
                    return board.BugMove(board_.name,board.Move(4,board.Board.HEIGHT-1,6,board.Board.HEIGHT-1,True,0))
            if p == "Q":
                if color == "W":
                    return board.BugMove(board_.name,board.Move(4,0,2,0,True,0))
                else:
                    return board.BugMove(board_.name,board.Move(4,board.Board.HEIGHT-1,2,board.Board.HEIGHT-1,True,0))
            else:
                print("Invalid castle format.")
                return get_move(dboard,color1,color2)
        if string[1] == "L":
            p = string[2]
            if p == "P":
                x2 = letter_to_digit(string[4])
                y2 = int(string[5])
                return board.BugMove(board_.name,board.PlacePiece(pieces.Pawn(color,board.Board.WIDTH,board.Board.HEIGHT),x2,y2-1))
            if p == "N":
                x2 = letter_to_digit(string[4])
                y2 = int(string[5])
                return board.BugMove(board_.name,board.PlacePiece(pieces.Knight(color,board.Board.WIDTH,board.Board.HEIGHT),x2,y2-1))
            if p == "B":
                x2 = letter_to_digit(string[4])
                y2 = int(string[5])
                return board.BugMove(board_.name,board.PlacePiece(pieces.Bishop(color,board.Board.WIDTH,board.Board.HEIGHT),x2,y2-1))
            if p == "R":
                x2 = letter_to_digit(string[4])
                y2 = int(string[5])
                return board.BugMove(board_.name,board.PlacePiece(pieces.Rook(color,board.Board.WIDTH,board.Board.HEIGHT),x2,y2-1))
            if p == "Q":
                x2 = letter_to_digit(string[4])
                y2 = int(string[5])
                return board.BugMove(board_.name,board.PlacePiece(pieces.Queen(color,board.Board.WIDTH,board.Board.HEIGHT),x2,y2-1))
            else:
                print("Invalid piece placement format.")
                return get_move(dboard,color1,color2)
        else: 
            print("First letter must be M,P,C, or L.")
            return get_move(dboard,color1,color2)

    except ValueError:
        print("Invalid format. Try again.")
        return get_move(dboard,color1,color2)

def letter_to_digit(letter):
    letter = letter.lower()
    if letter == 'a':
        return 0
    if letter == 'b':
        return 1
    if letter == 'c':
        return 2
    if letter == 'd':
        return 3
    if letter == 'e':
        return 4
    if letter == 'f':
        return 5
    if letter == 'g':
        return 6
    if letter == 'h':
        return 7

    raise ValueError("Invalid letter.")

def get_legal_move(dboard,color1,color2):
    real_legal_moves1 = dboard.rboard1.real_legal_moves(color1)
    real_legal_moves2 = dboard.rboard2.real_legal_moves(color2)
    for move in real_legal_moves1:
        print(move.to_string())
    for move in real_legal_moves2:
        print(move.to_string())
    is_legal = False
    if len(real_legal_moves1) == 0:
        is_legal = True
        return board.BugMove("1",board.PlacePiece("K",board.Board.WIDTH,board.Board.HEIGHT))
    elif len(real_legal_moves2) == 0:
        is_legal = True 
        return board.BugMove("2",board.PlacePiece("K",board.Board.WIDTH,board.Board.HEIGHT))
    else:
        while True:
            move = get_move(dboard,color1,color2)
            if move.rboardname == "Board1":
                real_legal_moves = real_legal_moves1 
            else:
                real_legal_moves = real_legal_moves2
            ## make real_legal_moves
            for candidate in real_legal_moves:
                if move == candidate:
                    print("Got it")
                    is_legal = True
                    break
            if is_legal == True:
                break
            if is_legal == False:
                print("Illegal move. Try again.")
        return move

dboard = board.DoubleBoard_standard_setup()
board1_turn = "W"
board2_turn = "W"
while True:
    print(dboard.to_string())
    move = get_legal_move(dboard,board1_turn,board2_turn)
    if move.rboardname == "1":
        (x,y) = dboard.rboard1.board.find_king(board1_turn)
        if not dboard.rboard1.in_check(board1_turn,x,y):
            print("Stalemate. Tie.")
        elif board1_turn == "W":
            ## check stalemate case
            print("Front team wins.")
            break 
        else:
            print("Back team wins.")
            break 
    if move.rboardname == "2":
        (x,y) = dboard.rboard2.board.find_king(board2_turn)
        if not dboard.rboard2.in_check(board1_turn,x,y):
            print("Stalemate. Tie.")
        elif board2_turn == "W":
            print("Back team wins.")
            break 
        else:
            print("Front team wins.")
            break 
    if move.rboardname == "Board1":
        dboard.do_move(move)
        if board1_turn == "W":
            print("On Board 1, White played" + move.to_string())
            board1_turn = "B"
        else:
            print("On Board 1, Black played" + move.to_string())
            board1_turn = "W"
    else:
        dboard.do_move(move)
        if board2_turn == "W":
            print("On Board 2, White played" + move.to_string())
            board2_turn = "B"
        else:
            print("On Board 2, Black played" + move.to_string())
            board2_turn = "W"