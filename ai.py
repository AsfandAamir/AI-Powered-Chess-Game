# ai.py
import copy
import random

MAX_DEPTH = 3

def evaluate_board(board):
    # Simple evaluation: +1 per white pawn, -1 per black pawn
    score = 0
    for row in board:
        for piece in row:
            if piece == 'wp':
                score += 1
            elif piece == 'bp':
                score -= 1
    return score

def get_all_moves(board, is_white):
    moves = []
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if (is_white and piece == 'wp') or (not is_white and piece == 'bp'):
                direction = -1 if is_white else 1
                new_r = r + direction
                if 0 <= new_r < 8:
                    if board[new_r][c] == '':
                        new_board = copy.deepcopy(board)
                        new_board[new_r][c] = piece
                        new_board[r][c] = ''
                        moves.append(new_board)
    return moves

def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0:
        return evaluate_board(board), board

    best_move = None
    moves = get_all_moves(board, maximizing)

    if maximizing:
        max_eval = float('-inf')
        for move in moves:
            eval, _ = minimax(move, depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in moves:
            eval, _ = minimax(move, depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def get_ai_move(board):
    _, move = minimax(board, MAX_DEPTH, float('-inf'), float('inf'), False)
    return move
