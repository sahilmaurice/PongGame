#  Pong Game

A modern Python Pong game built with Pygame featuring AI opponent and multiplayer modes.

##  Features

- **Single Player vs AI**: Play against an intelligent computer opponent
- **Multiplayer Mode**: Classic 2-player Pong experience
- **Smart AI**: Bot with ball prediction and adaptive difficulty
- **Smooth Gameplay**: 60 FPS with responsive controls
- **Game Mode Selection**: Easy menu system to choose your preferred mode
- **Restart Functionality**: Play multiple rounds without restarting

##  Installation

### Prerequisites
- Python 3.6 or higher
- Pygame

### Setup
```bash
# Clone the repository
git clone https://github.com/sahilmaurice/PongGame.git
cd PongGame

# Install Pygame (if not already installed)
pip install pygame

# Run the game
python ponggame.py
```

##  How to Play

### Game Modes
1. **Press `1`** - Single Player vs AI
2. **Press `2`** - Multiplayer (2 Players)

### Controls

#### Player 1 (Left Paddle)
- **W** - Move paddle up
- **S** - Move paddle down

#### Player 2 (Right Paddle) - Multiplayer Only
- **↑** (Up Arrow) - Move paddle up
- **↓** (Down Arrow) - Move paddle down

#### Game Controls
- **Space** - Start game / Restart after game over
- **Close Window** - Exit game

## Game Features

### AI Opponent
- Intelligent ball prediction
- Adaptive movement patterns
- Realistic difficulty progression
- Reliable first-ball hits

### Game Mechanics
- Ball bounces off paddles and walls
- Consistent ball speed throughout game
- Paddle boundary limits
- Winner detection and scoring

### Visual Design
- Clean, modern interface
- Color-coded paddles (Blue vs Red)
- White ball for clear visibility
- Intuitive menu system

## Game Rules

1. **Objective**: Prevent the ball from passing your paddle
2. **Scoring**: First player to let the ball pass loses
3. **Movement**: Paddles can move up and down within screen bounds
4. **Physics**: Ball bounces off paddles and top/bottom walls

## Technical Details

- **Engine**: Pygame
- **Language**: Python 3
- **Resolution**: 960x720 pixels
- **Frame Rate**: 60 FPS
- **AI**: Predictive ball tracking with randomness

## Tips for Players

- **Single Player**: The AI is designed to be challenging but beatable
- **Multiplayer**: Great for competitive play with friends
- **Paddle Control**: Use smooth movements for better accuracy
- **Ball Tracking**: Watch the ball's trajectory to predict its path

## Customization

You can easily modify game parameters in the code:
- Ball speed: Change `ball_accel_x` and `ball_accel_y` values
- Paddle speed: Adjust `paddle_1_move` and `paddle_2_move` values
- AI difficulty: Modify randomness values in the bot logic
- Colors: Change RGB values for different visual themes

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this repository and submit pull requests for improvements!

---

**Enjoy playing Pong! 🏓**
