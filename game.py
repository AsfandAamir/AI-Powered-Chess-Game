import pygame
import chess
import random
from utils import draw_board, load_piece_image

class Game:
    def __init__(self):
        self.board = chess.Board()
        self.selected_square = None
        self.player_color = chess.WHITE
        self.promotion_square = None
        self.promoting = False
        self.promotion_piece = chess.QUEEN
        self.promotion_move = None
        self.possible_moves = []  # List to hold the possible moves for the selected piece
        self.turn_count = 0  # Track the turn count

    def handle_click(self, pos, screen):
        row, col = pos[1] // 80, pos[0] // 80
        square = chess.square(col, 7 - row)

        if self.promoting:
            self.handle_promotion_click(pos)
            return

        if self.selected_square is None:
            piece = self.board.piece_at(square)
            if piece and piece.color == self.player_color:
                self.selected_square = square
                self.possible_moves = self.get_possible_moves(square)  # Get possible moves
        else:
            piece = self.board.piece_at(self.selected_square)
            is_promotion_rank = piece and piece.piece_type == chess.PAWN and chess.square_rank(square) in [0, 7]

            move = chess.Move(self.selected_square, square, promotion=chess.QUEEN if is_promotion_rank else None)

            if move in self.board.legal_moves:
                if is_promotion_rank:
                    self.promoting = True
                    self.promotion_square = square
                    self.promotion_move = move
                    return
                else:
                    self.board.push(move)
                    self.selected_square = None
                    self.possible_moves = []  # Clear possible moves after the move
                    self.turn_count += 1  # Increment turn count
                    if self.turn_count % 2 == 1:  # Player's turn
                        self.apply_piece_transformations()
                    self.ai_move()
                    self.check_game_status()
            else:
                self.selected_square = None
                self.possible_moves = []  # Clear possible moves if selection is canceled

    def handle_promotion_click(self, pos):
        x, y = pos
        if 100 <= x <= 240 and 300 <= y <= 360:
            self.promotion_piece = chess.QUEEN
        elif 250 <= x <= 390 and 300 <= y <= 360:
            self.promotion_piece = chess.ROOK
        elif 400 <= x <= 540 and 300 <= y <= 360:
            self.promotion_piece = chess.KNIGHT
        elif 550 <= x <= 690 and 300 <= y <= 360:
            self.promotion_piece = chess.BISHOP
        else:
            return

        promo = chess.Move(self.promotion_move.from_square, self.promotion_move.to_square, promotion=self.promotion_piece)
        if promo in self.board.legal_moves:
            self.board.push(promo)

        self.promoting = False
        self.promotion_square = None
        self.promotion_move = None
        self.selected_square = None
        self.ai_move()
        self.check_game_status()

    def ai_move(self):
        if self.board.is_game_over():
            return
        legal_moves = list(self.board.legal_moves)
        if legal_moves:
            move = random.choice(legal_moves)
            self.board.push(move)

    def check_game_status(self):
        if self.board.is_game_over():
            print("Game over:", self.board.result())
            self.reset_game()

    def reset_game(self):
        self.board = chess.Board()
        self.selected_square = None
        self.promotion_square = None
        self.promoting = False
        self.promotion_piece = chess.QUEEN
        self.promotion_move = None
        self.possible_moves = []  # Clear possible moves
        self.turn_count = 0  # Reset the turn count

    def draw(self, screen):
        draw_board(screen)
        self.draw_pieces(screen)
        if self.promoting:
            self.draw_promotion_prompt(screen)
        self.draw_possible_moves(screen)  # Draw the possible moves

    def draw_pieces(self, screen):
        piece_type_names = {
            chess.PAWN: "pawn",
            chess.KNIGHT: "knight",
            chess.BISHOP: "bishop",
            chess.ROOK: "rook",
            chess.QUEEN: "queen",
            chess.KING: "king"
        }

        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                col = chess.square_file(square)
                row = 7 - chess.square_rank(square)
                piece_name = ("w_" if piece.color == chess.WHITE else "b_") + piece_type_names[piece.piece_type]
                piece_image = load_piece_image(piece_name)
                if piece_image:
                    screen.blit(piece_image, (col * 80, row * 80))

    def draw_promotion_prompt(self, screen):
        font = pygame.font.SysFont("Arial", 32)
        pygame.draw.rect(screen, (30, 30, 30), pygame.Rect(90, 250, 620, 160))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(90, 250, 620, 160), 4)

        options = [("Queen", 100), ("Rook", 250), ("Knight", 400), ("Bishop", 550)]

        for label, x in options:
            pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(x, 300, 140, 60))
            text = font.render(label, True, (0, 0, 0))
            screen.blit(text, (x + 20, 315))

    def get_possible_moves(self, square):
        """Returns a list of legal moves for a piece at the given square."""
        possible_moves = []
        piece = self.board.piece_at(square)

        if piece:
            if self.turn_count % 3 == 0:
                # On every 3rd turn, modify the move generation to act like a transformed piece
                if piece.piece_type == chess.ROOK:
                    # Allow rook to move like a queen (straight and diagonal)
                    for move in self.board.legal_moves:
                        if move.from_square == square and (move.to_square in self.board.attacks(move.from_square) or chess.Move(square, move.to_square) in self.board.legal_moves):
                            possible_moves.append(move.to_square)
                else:
                    # For other pieces, get normal moves
                    for move in self.board.legal_moves:
                        if move.from_square == square:
                            possible_moves.append(move.to_square)
            else:
                for move in self.board.legal_moves:
                    if move.from_square == square:
                        possible_moves.append(move.to_square)
        return possible_moves

    def draw_possible_moves(self, screen):
        """Draws possible moves on the board (highlight squares)."""
        for square in self.possible_moves:
            col = chess.square_file(square)
            row = 7 - chess.square_rank(square)
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(col * 80, row * 80, 80, 80), 3)  # Highlight with green

    def apply_piece_transformations(self):
        """Apply transformations to pieces based on the rules for every 3rd turn."""
        if self.turn_count % 3 == 0:
            for square in chess.SQUARES:
                piece = self.board.piece_at(square)
                if piece:
                    if piece.color == self.player_color:
                        # Only modify pieces for the current player
                        if piece.piece_type == chess.ROOK:
                            self.board.set_piece_at(square, chess.Piece(chess.QUEEN, piece.color))
                        elif piece.piece_type == chess.QUEEN:
                            self.board.set_piece_at(square, chess.Piece(chess.BISHOP, piece.color))
                        elif piece.piece_type == chess.BISHOP:
                            self.board.set_piece_at(square, chess.Piece(chess.KNIGHT, piece.color))
                        elif piece.piece_type == chess.KNIGHT:
                            self.board.set_piece_at(square, chess.Piece(chess.ROOK, piece.color))
