import pygame

# Load piece images and store in a dictionary to avoid reloading
_piece_images = {}

def load_piece_image(piece_name):
    if piece_name not in _piece_images:
        try:
            image = pygame.image.load(f'assets/{piece_name}.png')
            image = pygame.transform.scale(image, (80, 80))
            _piece_images[piece_name] = image
        except FileNotFoundError:
            print(f"Image file for {piece_name} not found in assets folder.")
            _piece_images[piece_name] = None
    return _piece_images[piece_name]

def draw_board(screen):
    colors = [pygame.Color(240, 217, 181), pygame.Color(181, 136, 99)]  # light and dark squares
    square_size = 80

    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col * square_size, row * square_size, square_size, square_size))
