from chessPlayer_prelim import *


def chessPlayer(board, player):
    move = gen_minimax_move(board, player)
    if len(move) > 4:
        source, target = move[:2]
        evalTree = move[2].get_level_order()
        all_moves = move[3]
        scores = move[4]
        candidate_moves = []
        for i in range(len(scores)):
            candidate_moves += [[all_moves[i][1], all_moves[i][0], float(scores[i])]]
        return [True, [target, source], candidate_moves, evalTree]

    else:
        evalTree = move[1].get_level_order()
        all_moves = move[2]
        scores = move[3]
        candidate_moves = []
        for i in range(len(scores)):
            candidate_moves += [[all_moves[i][1], all_moves[i][0], float(scores[i])]]
        return [False, None, candidate_moves, evalTree]
