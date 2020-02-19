from chessPlayer_structs import *


# ------------------ CHESS INFO AND FUNCTIONS ---------------------------
def gen_board():
    board = [0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0]
    return board


def get_player_value(name):
    if name == "WHITE":
        return 10
    if name == "BLACK":
        return 20


def get_piece_value(name):
    if name == "PAWN":
        return 0
    elif name == "KNIGHT":
        return 1
    elif name == "BISHOP":
        return 2
    elif name == "ROOK":
        return 3
    elif name == "QUEEN":
        return 4
    elif name == "KING":
        return 5


def get_piece_weight(value):
    if value == get_piece_value("PAWN"):
        return 5
    elif value == get_piece_value("KNIGHT"):
        return 15
    elif value == get_piece_value("BISHOP"):
        return 15
    elif value == get_piece_value("ROOK"):
        return 17
    elif value == get_piece_value("QUEEN"):
        return 50
    elif value == get_piece_value("KING"):
        return 200


def get_player(space):
    return (space // 10) * 10


def get_enemy(player):
    if player == 10:
        return 20
    else:
        return 10


def get_piece(space):
    return space % 10


def get_row(position):
    return position // 8


def get_col(position):
    return position % 8


def get_index(row, col):
    return (row * 8) + col


def row_up(position, number=1):
    return position + number * 8


def row_down(position, number=1):
    return position - number * 8


def col_right(position, number=1):
    return position - number


def col_left(position, number=1):
    return position + number


def is_index_on_board(p):
    return 0 <= p < 64


def is_player(board, position, player):
    return get_player(board[position]) == player


def is_space_empty(board, position):
    return board[position] == 0


def off_board(direction, start, end):
    if direction == "UP":
        if start > end:
            return True
        else:
            return False
    elif direction == "DOWN":
        if start < end:
            return True
        else:
            return False
    elif direction == "LEFT":
        if start > end:
            return True
        else:
            return False
    elif direction == "RIGHT":
        if start < end:
            return True
        else:
            return False
    else:
        return False


# ------------------------------------------------------------------------------

# ------------------------- CHESS KNOWLEDGE -----------------------------------------
def get_player_positions(board, player):
    pos = []
    for r in range(8):
        for i in range(8):
            if get_player(board[get_index(r, i)]) == player:
                pos += [get_index(r, i)]
    return pos


def get_piece_legal_moves(board, position):
    pos = []
    player = get_player(board[position])
    enemy = get_enemy(player)
    piece = get_piece(board[position])
    row = get_row(position)
    space = get_col(position)
    if position > 64 or position < 0:
        return pos
    else:
        if board[position] == 0:
            return pos
        elif piece == get_piece_value("PAWN"):
            if player == get_player_value("WHITE"):
                p = row_up(get_index(row, space))
                if is_index_on_board(p) and is_space_empty(board, p) and not off_board("UP", row, get_row(p)):
                    pos += [p]
                capture_moves = get_pawn_capture_moves(board, get_index(row, space))
                p = capture_moves[0]
                if is_index_on_board(p) and is_player(board, p, enemy) and not off_board("UP", row, get_row(p)) \
                        and not off_board("RIGHT", space, get_col(p)):
                    pos += [p]
                p = capture_moves[1]
                if is_index_on_board(p) and is_player(board, p, enemy) and not off_board("UP", row, get_row(p)) \
                        and not off_board("LEFT", space, get_col(p)):
                    pos += [p]
            elif player == get_player_value("BLACK"):
                p = row_down(get_index(row, space))
                if is_index_on_board(p) and 0 == board[p] and not off_board("DOWN", row, get_row(p)):
                    pos += [p]
                capture_moves = get_pawn_capture_moves(board, get_index(row, space))
                p = capture_moves[0]
                if is_index_on_board(p) and is_player(board, p, enemy) and not off_board("DOWN", row, get_row(p)) \
                        and not off_board("RIGHT", space, get_col(p)):
                    pos += [p]
                p = capture_moves[1]
                if is_index_on_board(p) and is_player(board, p, enemy) and not off_board("DOWN", row, get_row(p)) \
                        and not off_board("LEFT", space, get_col(p)):
                    pos += [p]
        if piece == get_piece_value("KNIGHT"):
            temp = [[col_left(row_down(get_index(row, space), 2)), "LEFT", "DOWN"],
                    [col_right(row_down(get_index(row, space), 2)), "RIGHT", "DOWN"],
                    [col_left(row_up(get_index(row, space), 2)), "LEFT", "UP"],
                    [col_right(row_up(get_index(row, space), 2)), "RIGHT", "UP"],
                    [col_left(row_down(get_index(row, space)), 2), "LEFT", "DOWN"],
                    [col_right(row_down(get_index(row, space)), 2), "RIGHT", "DOWN"],
                    [col_left(row_up(get_index(row, space)), 2), "LEFT", "UP"],
                    [col_right(row_up(get_index(row, space)), 2), "RIGHT", "UP"]]
            for p in temp:
                if is_index_on_board(p[0]) and not is_player(board, p[0], player) \
                        and not off_board(p[1], space, get_col(p[0])) and not off_board(p[2], row, get_row(p[0])):
                    pos += [p[0]]
        if piece == get_piece_value("BISHOP") or piece == get_piece_value("QUEEN"):
            p = col_left(row_up(get_index(row, space)))
            while is_index_on_board(p) and not is_player(board, p, player) and not off_board("UP", row, get_row(p)) \
                    and not off_board("LEFT", space, get_col(p)):
                pos += [p]
                if get_col(p) == 7:
                    break
                if is_player(board, p, enemy):
                    break
                p = col_left(row_up(p))

            p = col_right(row_up(get_index(row, space)))
            while is_index_on_board(p) and not is_player(board, p, player) and not off_board("UP", row, get_row(p)) \
                    and not off_board("RIGHT", space, get_col(p)):
                pos += [p]
                if get_col(p) == 0:
                    break
                if is_player(board, p, enemy):
                    break
                p = col_right(row_up(p))

            p = col_right(row_down(get_index(row, space)))
            while is_index_on_board(p) and not is_player(board, p, player) and not off_board("DOWN", row, get_row(p)) \
                    and not off_board("RIGHT", space, get_col(p)):
                pos += [p]
                if get_col(p) == 0:
                    break
                if is_player(board, p, enemy):
                    break
                p = col_right(row_down(p))

            p = col_left(row_down(get_index(row, space)))
            while is_index_on_board(p) and not is_player(board, p, player) and not off_board("DOWN", row, get_row(p)) \
                    and not off_board("LEFT", space, get_col(p)):
                pos += [p]
                if get_col(p) == 7:
                    break
                if is_player(board, p, enemy):
                    break
                p = col_left(row_down(p))
        if piece == get_piece_value("ROOK") or piece == get_piece_value("QUEEN"):
            p = row_up(get_index(row, space))
            while is_index_on_board(p) and not is_player(board, p, player) and not off_board("UP", row, get_row(p)):
                pos += [p]
                if is_player(board, p, enemy):
                    break
                p = row_up(p)
            p = row_down(get_index(row, space))
            while is_index_on_board(p) and not is_player(board, p, player) and not off_board("DOWN", row, get_row(p)):
                pos += [p]
                if is_player(board, p, enemy):
                    break
                p = row_down(p)
            p = col_left(get_index(row, space))
            while is_index_on_board(p) and not is_player(board, p, player) and not off_board("LEFT", space, get_col(p)):
                pos += [p]
                if get_col(p) == 7:
                    break
                if is_player(board, p, enemy):
                    break
                p = col_left(p)
            p = col_right(get_index(row, space))
            while is_index_on_board(p) and not is_player(board, p, player) and not off_board("RIGHT", space,
                                                                                             get_col(p)):
                pos += [p]
                if get_col(p) == 0:
                    break
                if is_player(board, p, enemy):
                    break
                p = col_right(p)
        if piece == get_piece_value("KING"):
            p = row_up(get_index(row, space))
            if is_index_on_board(p) and not is_player(board, p, player) and not off_board("UP", row, get_row(p)):
                pos += [p]
            p = row_down(get_index(row, space))
            if is_index_on_board(p) and not is_player(board, p, player) and not off_board("DOWN", row, get_row(p)):
                pos += [p]
            p = col_left(get_index(row, space))
            if is_index_on_board(p) and not is_player(board, p, player) and not off_board("LEFT", space, get_col(p)):
                pos += [p]
            p = col_right(get_index(row, space))
            if is_index_on_board(p) and not is_player(board, p, player) and not off_board("RIGHT", space, get_col(p)):
                pos += [p]
            p = col_left(row_up(get_index(row, space)))
            if is_index_on_board(p) and not is_player(board, p, player) and not off_board("UP", row, get_row(p)) \
                    and not off_board("LEFT", space, get_col(p)):
                pos += [p]
            p = col_right(row_down(get_index(row, space)))
            if is_index_on_board(p) and not is_player(board, p, player) and not off_board("DOWN", row, get_row(p)) \
                    and not off_board("RIGHT", space, get_col(p)):
                pos += [p]
            p = col_right(row_up(get_index(row, space)))
            if is_index_on_board(p) and not is_player(board, p, player) and not off_board("UP", row, get_row(p)) \
                    and not off_board("RIGHT", space, get_col(p)):
                pos += [p]
            p = col_left(row_down(get_index(row, space)))
            if is_index_on_board(p) and not is_player(board, p, player) and not off_board("DOWN", row, get_row(p)) \
                    and not off_board("LEFT", space, get_col(p)):
                pos += [p]
        return pos


def get_pawn_capture_moves(board, position):
    player = get_player(board[position])
    moves = []
    if player == get_player_value("WHITE"):
        moves += [col_right(row_up(position))]
        moves += [col_left(row_up(position))]
    else:
        moves += [col_right(row_down(position))]
        moves += [col_left(row_down(position))]
    return moves


def is_position_under_threat(board, position, player):
    enemy = get_enemy(player)
    for p in get_player_positions(board, enemy):
        if get_piece(board[p]) == get_piece_value("PAWN"):
            pos = get_pawn_capture_moves(board, p)
        else:
            pos = get_piece_legal_moves(board, p)
        for s in pos:
            if s == position:
                return True
    return False


# ----------------------------------------------------------------------------------

def get_player_moves_list(board, player):
    pos = get_player_positions(board, player)
    non_losing_moves = []
    all_moves = []
    for source in pos:
        moves = get_piece_legal_moves(board, source)
        for move in moves:
            all_moves += [[source, move]]
            if not (is_position_under_threat(board, move, player)):
                non_losing_moves += [[source, move]]
    return [non_losing_moves, all_moves]


def is_checkmate(board, player):
    positions = get_player_positions(board, player)
    for p in positions:
        if get_piece(board[p]) == get_piece_value("KING"):
            if is_position_under_threat(board, p, player):
                for move in get_piece_legal_moves(board, p):
                    if not is_position_under_threat(board, move, player):
                        return False
                return True
    return False


def is_draw(board):
    if 0 == len(get_player_moves_list(board, get_player_value("WHITE"))) == \
            len(get_player_moves_list(board, get_player_value("BLACK"))) and not \
            is_checkmate(board, get_player_value("WHITE")) and not is_checkmate(board, get_player_value("BLACK")):
        return True
    else:
        return False


def move_piece(board, source, target):
    if not is_space_empty(board, target):
        collected = get_piece(board[target])
    else:
        collected = -1
    board[target] = board[source]
    board[source] = 0
    return collected


def make_test_board(board, source, target):
    new_board = list(board)
    move_piece(new_board, source, target)
    return new_board


def get_piece_mobility_factor(board, position):
    piece = get_piece(board[position])
    b_board = gen_board()
    b_board[get_index(3, 3)] = piece + 10
    max_moves = get_piece_legal_moves(b_board, get_index(3, 3))
    moves = get_piece_legal_moves(board, position)
    return len(moves) / len(max_moves)


def eval_board_1(board):
    white_pos = get_player_positions(board, get_player_value("WHITE"))
    black_pos = get_player_positions(board, get_player_value("BLACK"))
    score = 0
    for pos in white_pos:
        piece = get_piece(board[pos])
        score += get_piece_mobility_factor(board, pos) * (piece + 10)
    for pos in black_pos:
        piece = get_piece(board[pos])
        score -= get_piece_mobility_factor(board, pos) * (piece + 10)
    return score


def eval_board_2(board):
    white_pos = get_player_positions(board, get_player_value("WHITE"))
    black_pos = get_player_positions(board, get_player_value("BLACK"))
    score = 0
    for pos in white_pos:
        score += get_piece_weight(get_piece(board[pos])) + 0.1 * len(get_piece_legal_moves(board, pos))
    for pos in black_pos:
        score -= (get_piece_weight(get_piece(board[pos])) + 0.1 * len(get_piece_legal_moves(board, pos)))
    return score


def get_max_or_min(best, score, best_item, item, player):
    if player == get_player_value("WHITE"):
        if score >= best:
            best = score
            best_item = item
    elif player == get_player_value("BLACK"):
        if score <= best:
            best = score
            best_item = item
    return [best, best_item]


def gen_reflex_agent_move(board, player):
    non_losing_moves, all_moves = get_player_moves_list(board, player)
    best = -float("inf")
    move = []
    for source, target in non_losing_moves:
        score = eval_board_2(make_test_board(board, source, target))
        best, move = get_max_or_min(best, score, move, [source, target], player)
    return move


def build_game_tree(player, game_tree: Tree, levels):
    if levels == 3:
        return True
    else:
        enemy = get_enemy(player)
        board = game_tree.get_val()[0]
        non_losing_moves, all_moves = get_player_moves_list(board, player)
        for move in all_moves:
            game_tree.add_child([make_test_board(board, move[0], move[1]), move])

        for child in game_tree.get_children():
            build_game_tree(enemy, child, levels + 1)
    return all_moves


def minimax(node: Tree, player):
    enemy = get_enemy(player)
    is_max = player == get_player_value("WHITE")

    if node.is_leaf() or is_checkmate(node.get_val()[0], player) or is_checkmate(node.get_val()[0], enemy) or is_draw(
            node.get_val()[0]):
        max_score = eval_board_2(node.get_val()[0])
        return [max_score, [0, 0]]

    scores = [minimax(child, enemy)[0] for child in node.get_children()]
    max_score = max(scores) if is_max else min(scores)
    best_indices = [index for index in range(len(node.get_children())) if scores[index] == max_score]
    chosen_index = best_indices[0]
    chosen_node = node.get_children()[chosen_index]

    return max_score, chosen_node.get_val()[1], scores


def gen_minimax_move(board, player):
    game_tree = Tree([board, [0, 0]])
    all_moves = build_game_tree(player, game_tree, 1)
    best, best_move, scores = minimax(game_tree, player)
    if not (len(best_move) > 0):
        return best_move, game_tree, all_moves, scores
    return [best_move[0], best_move[1], game_tree, all_moves, scores]
