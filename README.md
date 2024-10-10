# N Puzzle Game

The 15-puzzle is a sliding puzzle that consists of a frame of numbered square tiles in random
order with one tile missing. Game is represented by 4x4 tiles(or 3x3 etc) board where N numbered tiles are
initially placed in random order and where 16th tile is missing. A tile can be moved to a
neighbour empty place. To succeed in the game you need to order tiles from 1 to 15, where tile
number 1 is at the top left corner and empty one is at the bottom right corner.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)


## Installation

Instructions on how to install and set up the project.

```bash
# Clone the repository
https://github.com/TarasOnyshchenkoDev/NPuzzleGame.git

# Navigate to the project directory
cd NPuzzleGame
```
## Usage
```bash
# Run project
# go to main.py and configure board dimensions
# (4 by 4 is default one, but can be change in range from 2 to 100)
python main.py

#Run tests
python -m unittest discover test

```