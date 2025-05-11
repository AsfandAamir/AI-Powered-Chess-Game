# AI-Powered Chess Game 

Welcome to the **AI-Powered Chess Game**, a fun and interactive chess application developed in Python using `pygame` and `python-chess`. This chess game features:

- Classic 8x8 board with polished UI
- Human vs AI gameplay
- Pawn promotion UI
- Unique gameplay mechanic: every 3rd player turn, piece transformations occur (e.g., Rook becomes Queen)
- Move highlighting for better user experience

## 🔧 Features

- 🎮 Play against a simple AI
- ✨ Promotion panel (choose between Queen, Rook, Bishop, Knight)
- ♻️ Piece transformation every 3rd turn:
  - Rook → Queen → Bishop → Knight → Rook (cycle)
- ✅ Legal move highlighting for selected pieces
- 🔁 Game resets automatically on checkmate/stalemate

## 📹 Demo

Watch the full demonstration of this project on YouTube:  
📺 [YouTube Demo](https://youtu.be/M7znA2Zy6es)

## 🚀 Installation

### Prerequisites

- Python 3.8+
- `pygame`
- `python-chess`

### Install dependencies

pip install pygame python-chess

### Run the game

python main.py


## 🗂️ Project Structure

AI-Powered-Chess-Game/
│
├── main.py                # Entry point

├── game.py                # Game logic and rendering

├── utils.py               # Helper functions (e.g., draw_board, load_piece_image)

├── images/                # Piece images (e.g., w_pawn.png, b_queen.png, etc.)

├── README.md              # Project documentation



## 📦 Features in `game.py`

- Board drawing with `pygame`
- Handling piece selection and highlighting
- Legal move generation with `python-chess`
- Piece transformation logic on every 3rd turn
- AI opponent making random legal moves


## 👨‍💻 Author

Developed by [Asfand Aamir](https://github.com/AsfandAamir)


