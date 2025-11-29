# Adventure Game - Udacity Introduction to Programming with Python I

A text-based adventure game where you navigate through different locations, encounter enemies, and fight for survival!

## Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) - A fast Python package installer and resolver

## Installing uv

If you don't have `uv` installed, you can install it using one of the following methods:

### macOS and Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Using pip
```bash
pip install uv
```

For more installation options, visit the [uv documentation](https://github.com/astral-sh/uv).

## Project Setup

1. **Clone or navigate to the project directory:**
   ```bash
   cd 1-learning-programming-python
   ```

2. **Install dependencies using uv:**
   ```bash
   uv sync
   ```
   This command will:
   - Create a virtual environment (if it doesn't exist)
   - Install all dependencies specified in `pyproject.toml`
   - Lock the dependencies in `uv.lock`

3. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate  # On Windows
   ```

   Alternatively, you can run commands directly with `uv run` without activating the environment.

## Running the Adventure Game

### Method 1: Using uv run (Recommended)
```bash
uv run python adventure_game.py
```

This command automatically uses the project's virtual environment and runs the game.

### Method 2: Using the activated virtual environment
If you've activated the virtual environment:
```bash
python adventure_game.py
```

## How to Play

1. **Start the game:** Run the game using one of the methods above.

2. **Choose your character:** You'll be randomly assigned a character (knight, troll, or villain).

3. **Navigate locations:** When prompted, enter the number corresponding to the location you want to visit.

4. **Encounter enemies:** As you explore, you'll encounter various enemies (knights, trolls, villains, dragons, or fairies).

5. **Survive battles:** Each encounter has a risk of death. Survive to continue your journey!

6. **Win condition:** Survive 20 turns to win the game.

7. **Play again:** After the game ends, you'll be asked if you want to play again.

## Game Features

- **Multiple locations:** Explore castles, caves, villages, rivers, woods, open fields, ancient fortresses, and ruins
- **Dynamic encounters:** Different locations have different probabilities of encountering various enemies
- **Risk-based combat:** Each enemy encounter has a calculated risk of death based on your character type
- **Turn-based gameplay:** Navigate through locations turn by turn
- **Replayability:** Play multiple times with different outcomes

## Project Structure

```
1-learning-programming-python/
├── adventure_game.py    # Main game file
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock              # Locked dependency versions
└── README.md            # This file
```

## Troubleshooting

### If `uv` command is not found:
- Make sure `uv` is installed and added to your PATH
- Try restarting your terminal
- On macOS/Linux, you may need to add `~/.cargo/bin` to your PATH

### If you get Python version errors:
- Ensure you have Python 3.12 or higher installed
- Check your Python version with: `python --version` or `python3 --version`

### If dependencies fail to install:
- Try updating `uv`: `uv self update`
- Delete `.venv` directory and `uv.lock` file, then run `uv sync` again

## Notes

- The game uses a random seed (42) for reproducible testing. You can modify this in `adventure_game.py` if you want different outcomes each run.
- The game includes error handling for invalid inputs and missing configurations.
- Maximum turn limit is set to 20 to prevent infinite gameplay loops.

## License

This project is part of the Udacity Introduction to Programming with Python I course.

