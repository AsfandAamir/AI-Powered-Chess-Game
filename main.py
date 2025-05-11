import pygame
import sys
from game import Game

pygame.init()
WIDTH, HEIGHT = 900, 740
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)
small_font = pygame.font.SysFont("Arial", 28)

# Color scheme
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (40, 44, 52)
DARK_BUTTON = (60, 63, 65)
HOVER = (85, 90, 95)

# Game state
game_state = "menu"  # menu, rules, game
game = Game()

def draw_text_center(text, y, font_obj, color=WHITE):
    label = font_obj.render(text, True, color)
    screen.blit(label, ((WIDTH - label.get_width()) // 2, y))

def draw_button(text, rect, hovered):
    pygame.draw.rect(screen, HOVER if hovered else DARK_BUTTON, rect)
    pygame.draw.rect(screen, WHITE, rect, 2)
    label = font.render(text, True, WHITE)
    screen.blit(label, (rect.x + 20, rect.y + 10))

# Button rects
start_button = pygame.Rect(300, 200, 200, 60)
rules_button = pygame.Rect(300, 300, 200, 60)
exit_button = pygame.Rect(300, 400, 200, 60)

def draw_menu():
    screen.fill(DARK_GRAY)
    draw_text_center("Welcome to Chess", 100, font, WHITE)
    mouse_pos = pygame.mouse.get_pos()

    draw_button("Start Game", start_button, start_button.collidepoint(mouse_pos))
    draw_button("Rules", rules_button, rules_button.collidepoint(mouse_pos))
    draw_button("Exit", exit_button, exit_button.collidepoint(mouse_pos))

def draw_rules():
    screen.fill(DARK_GRAY)
    rules = [
        "Chess Rules:",
        "Standard Chess Base: The game is based on classic chess rules.",
        "Turn-Based Play: Players alternate turns, starting with White.",
        "Every 3rd Turn Twist: On 3rd turn (your turn only),", 
        "your pieces transform:",
        "Rook → Queen",
        "Queen → Bishop",
        "Bishop → Knight",
        "Knight → Rook",
        "Move Highlighting: Clicking a piece shows all legal moves with green highlights.",
        "Pawn Promotion: When reaching the last rank,", 
        "choose to promote to Queen, Rook, Knight, or Bishop.",
        "AI Opponent: After your move, the AI will make a random legal move.",
        "Game Over: When checkmate, stalemate, or draw occurs, the game resets.",
        "",
        "Click anywhere to return to menu."
    ]
    for i, line in enumerate(rules):
        draw_text_center(line, 80 + i * 40, small_font, WHITE)

# --- Main Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    game_state = "game"
                elif rules_button.collidepoint(event.pos):
                    game_state = "rules"
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        elif game_state == "rules":
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_state = "menu"

        elif game_state == "game":
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(event.pos, screen)

    # Draw current state
    if game_state == "menu":
        draw_menu()
    elif game_state == "rules":
        draw_rules()
    elif game_state == "game":
        game.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
