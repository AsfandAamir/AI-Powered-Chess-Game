# pieces.py

# This module defines basic structure for pieces, mainly to support expansion
# For now, we only define Pawns with potential for adding more custom logic

class Piece:
    def __init__(self, color, name):
        self.color = color  # 'w' or 'b'
        self.name = name    # 'p' for pawn (can be 'q', 'k', etc. later)

    def __str__(self):
        return self.color + self.name

    def valid_moves(self, board, r, c):
        moves = []
        direction = -1 if self.color == 'w' else 1
        new_r = r + direction
        if 0 <= new_r < 8 and board[new_r][c] == '':
            moves.append((new_r, c))
        return moves

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, 'p')

    def bonus_ability(self, row):
        # Placeholder for pawn's custom ability when on certain rank
        if (self.color == 'w' and row == 3) or (self.color == 'b' and row == 4):
            return True
        return False
