from chessPlayer import *
from time import time


# ---------------------------- GAME SET-UP -----------------------
def set_board(board):
    for r in range(8):
        for i in range(8):
            if r < 2:
                board[get_index(r, i)] = get_player_value("WHITE")
            elif r > 5:
                board[get_index(r, i)] = get_player_value("BLACK")
            else:
                board[get_index(r, i)] = 0

    board[get_index(0, 0)] += get_piece_value("ROOK")
    board[get_index(0, 7)] += get_piece_value("ROOK")
    board[get_index(7, 0)] += get_piece_value("ROOK")
    board[get_index(7, 7)] += get_piece_value("ROOK")

    board[get_index(0, 1)] += get_piece_value("KNIGHT")
    board[get_index(0, 6)] += get_piece_value("KNIGHT")
    board[get_index(7, 1)] += get_piece_value("KNIGHT")
    board[get_index(7, 6)] += get_piece_value("KNIGHT")

    board[get_index(0, 2)] += get_piece_value("BISHOP")
    board[get_index(0, 5)] += get_piece_value("BISHOP")
    board[get_index(7, 2)] += get_piece_value("BISHOP")
    board[get_index(7, 5)] += get_piece_value("BISHOP")

    board[get_index(0, 3)] += get_piece_value("QUEEN")
    board[get_index(0, 4)] += get_piece_value("KING")
    board[get_index(7, 4)] += get_piece_value("QUEEN")
    board[get_index(7, 3)] += get_piece_value("KING")
    return 1


def clear_board(board):
    for i in range(len(board)):
        board[i] = 0


def print_board(board):
    cnt = 0
    pcnt1 = 0
    pcnt2 = 0
    rcnt1 = 0
    rcnt2 = 0
    kcnt1 = 0
    kcnt2 = 0
    bcnt1 = 0
    bcnt2 = 0
    row_cnt = 7
    label = "    7    6    5    4    3    2    1    0 "
    print(label)
    print(str(row_cnt) + " ", end="")
    for space in board[::-1]:
        if cnt == 8:
            print("", end="\n")
            row_cnt -= 1
            print(str(row_cnt) + " ", end="")
            cnt = 0

        piece = get_piece(space)
        player = get_player(space) // 10
        if space == 0:
            print(" --- ", end="")
        elif space == -1:
            print(" POS ", end="")
        elif piece == get_piece_value("PAWN"):
            if player == 1:
                pcnt1 += 1
                print(" " + str(player) + "P" + str(pcnt1) + " ", end="")
            elif player == 2:
                pcnt2 += 1
                print(" " + str(player) + "P" + str(pcnt2) + " ", end="")
        elif piece == get_piece_value("ROOK"):
            if player == 1:
                rcnt1 += 1
                print(" " + str(player) + "R" + str(rcnt1) + " ", end="")
            elif player == 2:
                rcnt2 += 1
                print(" " + str(player) + "R" + str(rcnt2) + " ", end="")
        elif piece == get_piece_value("KNIGHT"):
            if player == 1:
                kcnt1 += 1
                print(" " + str(player) + "K" + str(kcnt1) + " ", end="")
            elif player == 2:
                kcnt2 += 1
                print(" " + str(player) + "K" + str(kcnt2) + " ", end="")
        elif piece == get_piece_value("BISHOP"):
            if player == 1:
                bcnt1 += 1
                print(" " + str(player) + "B" + str(bcnt1) + " ", end="")
            elif player == 2:
                bcnt2 += 1
                print(" " + str(player) + "B" + str(bcnt2) + " ", end="")
        elif piece == get_piece_value("QUEEN"):
            print(" " + str(player) + "QU" + " ", end="")
        elif piece == get_piece_value("KING"):
            print(" " + str(player) + "KI" + " ", end="")
        cnt += 1
    print()
    print()
    return


# ------------------------- GAME LOGISTICS -----------------------------------------
def is_legal_move(board, source, target):
    pos = get_piece_legal_moves(board, source)
    for move in pos:
        if move == target:
            return True
    return False


def is_game_over(board):
    if is_draw(board) or is_checkmate(board, 10) or is_checkmate(board, 20):
        return True
    else:
        return False


def piece_count(board):
    white = len(get_player_positions(board, 10))
    black = len(get_player_positions(board, 20))
    return [white, black]


def test_game():
    board = gen_board()
    set_board(board)
    print_board(board)
    round = 1
    w_collection = []
    w_points = 0
    b_collection = []
    b_points = 0
    while round < 26:
        print('Round: ' + str(round))
        start = time()
        move = chessPlayer(board, 10)[1]
        end = time()
        print("Duration: " + str(end - start) + "s")
        if len(move) > 0:
            target, source = move
            if is_legal_move(board, source, target):
                c = move_piece(board, source, target)
                w_collection += [c + 1]
                print("White has moved")
                print_board(board)
                if is_game_over(board):
                    print("GAME OVER")
                    break
                if c == get_piece_value("KING"):
                    print("GAME OVER, KING DEAD")
                    break
            else:
                print("White has made an illegal move. " + str(source) + " " + str(target))
                break
        else:
            print("White cannot move")
            break

        # print("Source (r,c)?")
        # temp = input()
        # src_row, src_col = temp.split(",")
        # src_row, src_col = int(src_row), int(src_col)
        # source = get_index(src_row, src_col)
        #
        # print("Target (r,c)?")
        # temp = input()
        # tar_row, tar_col = temp.split(",")
        # tar_row, tar_col = int(tar_row), int(tar_col)
        # target = get_index(tar_row, tar_col)
        #
        # if is_legal_move(board, source, target):
        #     c = move_piece(board, source, target)
        #     w_collection += [c + 1]
        #     print("White has moved")
        #     print_board(board)
        #     if is_game_over(board):
        #         print("GAME OVER")
        #         break
        #     if c == get_piece_value("KING"):
        #         print("GAME OVER, KING DEAD")
        #         break
        #     print_board(board)
        #     white, black = piece_count(board)
        #     print(f"White Pieces: {white} Black Pieces: {black}")
        start = time()
        move = chessPlayer(board, 20)[1]
        end = time()
        print("Duration: " + str(end - start) + "s")
        if len(move) > 0:
            target, source = move
            if is_legal_move(board, source, target):
                c = move_piece(board, source, target)
                b_collection += [c + 1]
                print("Black has moved")
                print_board(board)
                if is_game_over(board):
                    print("GAME OVER")
                    break
                if c == get_piece_value("KING"):
                    print("GAME OVER, KING DEAD")
                    break
            else:
                print("Black has made an illegal move. " + str(source) + " " + str(target))
                break
        else:
            print("Black cannot move")
            break
        white, black = piece_count(board)
        print("White Pieces:" + str(white) + "Black Pieces:" + str(black))
        round += 1

    for c in w_collection:
        w_points += c
    for c in b_collection:
        b_points += c
    print("White Points:" + str(w_points) + "Black Points:" + str(b_points))


def test_pos():
    board = gen_board()
    for i in range(6):
        board[get_index(4, 4)] = i + 20
        for pos in get_piece_legal_moves(board, get_index(4, 4)):
            board[pos] = -1
        print_board(board)
        clear_board(board)
        board[get_index(0, 7)] = i + 20
        for pos in get_piece_legal_moves(board, get_index(0, 7)):
            board[pos] = -1
        print_board(board)
        clear_board(board)
        board[get_index(0, 0)] = i + 20
        for pos in get_piece_legal_moves(board, get_index(0, 0)):
            board[pos] = -1
        print_board(board)
        clear_board(board)
        board[get_index(7, 0)] = i + 20
        for pos in get_piece_legal_moves(board, get_index(7, 0)):
            board[pos] = -1
        print_board(board)
        clear_board(board)
        board[get_index(7, 7)] = i + 20
        for pos in get_piece_legal_moves(board, get_index(7, 7)):
            board[pos] = -1
        print_board(board)


if __name__ == '__main__':
    test_game()
