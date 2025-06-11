# Breakout Elite - Stanford Code in Place 2025
A modern, feature-rich implementation of the classic Breakout game with enhanced graphics, particle effects, power-ups, and smooth gameplay.

**Final Project Submission for Stanford Code in Place 2025**  
*Submitted by: Ahmed M. Fayad*

## Project Structure
The project has been organized into multiple modules for better maintainability and code organization:

### Core Files
- **`main.py`** - Main entry point and game orchestration
- **`config.py`** - All game configuration constants and settings
- **`game_objects.py`** - Game object classes (Particle, PowerUp, GameState)
- **`game_creation.py`** - Functions for creating game objects (bricks, paddle, ball)
- **`physics.py`** - Physics calculations and collision detection
- **`game_logic.py`** - Main game loop and turn logic
- **`visuals.py`** - Visual effects, UI components, and particle systems

## Features

### Enhanced Gameplay
- **Multi-turn System**: Play multiple rounds with cumulative scoring
- **Combo System**: Chain brick destructions for bonus points
- **Power-ups**: Collect falling power-ups for special abilities
  - 🔄 **Expand**: Increases paddle size
  - ⚡ **Speed**: Slows down ball for easier control
  - ✦ **Multi**: Future feature for multiple balls

### Visual Effects
- **Particle Explosions**: Dynamic particle effects when bricks are destroyed
- **Enhanced Graphics**: Gradient bricks, highlighted paddles and balls
- **Starfield Background**: Animated star field for ambiance
- **Universal Color Scheme**: Colors that work well on both light and dark backgrounds

### Game Mechanics
- **Physics-based Ball Movement**: Realistic ball physics with spin effects
- **Smart Paddle Control**: Mouse-controlled paddle with collision-based spin
- **Progressive Scoring**: Different point values for different brick rows
- **Win/Loss Conditions**: Clear all bricks to win, lose ball to lose turn

## How to Run
1. Ensure you have the `graphics.py` library available
2. Run the main game file:
   ```bash
   python main.py
   ```

## Code Organization Benefits

### Separation of Concerns
- **Configuration**: All constants in one place for easy tweaking
- **Game Objects**: Clean class definitions with clear responsibilities  
- **Physics**: Isolated collision detection and movement calculations
- **Visuals**: All UI and effects code separated from game logic
- **Creation**: Object instantiation logic kept separate from game loop

### Maintainability
- **Modular Design**: Easy to modify individual components without affecting others
- **Clear Dependencies**: Each module has well-defined imports and responsibilities
- **Scalable Architecture**: Easy to add new features like additional power-ups or game modes

### Code Reusability
- **Shared Constants**: Universal color scheme and game settings
- **Utility Functions**: Reusable functions for common operations
- **Object-Oriented Design**: Classes can be extended for new functionality

## Extending the Game

### Adding New Power-ups
1. Add the power-up type to `POWERUP_COLORS` and `POWERUP_SYMBOLS` in `config.py`
2. Implement the effect in `GameState.apply_powerup()` in `game_objects.py`
3. Add the power-up to the random selection in `game_logic.py`

### Adding New Visual Effects
1. Create new particle types in `game_objects.py`
2. Add visual functions to `visuals.py`
3. Integrate effects into the game loop in `game_logic.py`

### Modifying Game Balance
1. Adjust constants in `config.py`
2. Modify scoring logic in `game_logic.py`
3. Update physics parameters in `physics.py`

## Dependencies
- `graphics.py` - Graphics library for canvas operations
- Standard Python libraries: `time`, `random`, `math`

## Game Controls
- **Mouse**: Control paddle position
- **Click**: Start game and advance through screens

---

*This project represents the culmination of my learning journey in Stanford Code in Place 2025, incorporating concepts from Karel programming, Python fundamentals, control flow, graphics, data structures, and advanced programming techniques learned throughout the course.*

Enjoy playing Breakout Elite!
