# Bughouse
Bughouse Chess Game with AI
## Tech stack
- Object Oriented Programming

## File structure
```
|--- public ---|--- board // Bughouse board implementation
               |--- game // two-player Bughouse game (no AI)
               |--- pieces // Basic moves and special rules
```

# Packages and dependencies

# Progress
## Python (First Commit)
- [x] Chessboard
  - [x] Regular Chess Board
    - [x] Gets position
    - [x] Performs move
      - [x] Regular moves
      - [x] En passant moves
      - [x] Promotion moves
    - [x] Checks if moves are legal
      - [x] Checks if king is in check
  - [x] Bughouse Board Extension
    - [x] When pieces get captured, the partner gets it
    - [x] Board looks like an ugly string
  - [x] Clones board
- [x] Game mechanics
  - [x] Players put in strings as moves
  - [x] Game results
    - [x] When one team wins, the game stops
    - [x] Implemented stalemate
  - [ ] Bonus features
    - [ ] Undo move
    - [ ] Create save game
    - [ ] Create records of movements
- [x] Chess Pieces
  - [x] Pawn rules
    - [x] Pawn moves
      - [x] Implemented non-captures
      - [x] Implemented captures
      - [x] Implemented promotion
      - [x] Implemented en passant
    - [x] Implemented clone
  - [x] Knight rules
    - [x] Implemented L-shaped moves
    - [x] Implemented clone
  - [x] Bishop rules
    - [x] Implemented diagonal moves
    - [x] Implemented clone
  - [x] Rook rules
    - [x] Implemented lateral moves
    - [x] Implemented clone
  - [x] Queen rules
    - [x] Implemented diagonal moves
    - [x] Implemented lateral moves
    - [x] Implemented clone
  - [x] King rules 
    - [x] Implemented one-step moves
    - [x] Implemented castling
    - [x] Implemented clone

## Javascript Back End (Current Progress)
- [ ] Chessboard
  - [ ] Regular Chess Board
    - [ ] Gets position
    - [ ] Performs move
      - [ ] Regular moves
      - [ ] En passant moves
      - [ ] Promotion moves
    - [ ] Checks if moves are legal
      - [ ] Checks if king is in check
  - [ ] Bughouse Board Extension
    - [ ] When pieces get captured, the partner gets it
    - [ ] Board looks like an ugly string
  - [ ] Clones board
- [ ] Game mechanics
  - [ ] Players put in strings as moves
  - [ ] Game results
    - [ ] When one team wins, the game stops
    - [ ] Implemented stalemate
  - [ ] Bonus features
    - [ ] Undo move
    - [ ] Create save game
    - [ ] Create records of movements
- [ ] Chess Pieces
  - [ ] Pawn rules
    - [ ] Pawn moves
      - [ ] Implemented non-captures
      - [ ] Implemented captures
      - [ ] Implemented promotion
      - [ ] Implemented en passant
    - [ ] Implemented clone
  - [ ] Knight rules
    - [ ] Implemented L-shaped moves
    - [ ] Implemented clone
  - [ ] Bishop rules
    - [ ] Implemented diagonal moves
    - [ ] Implemented clone
  - [ ] Rook rules
    - [ ] Implemented lateral moves
    - [ ] Implemented clone
  - [ ] Queen rules
    - [ ] Implemented diagonal moves
    - [ ] Implemented lateral moves
    - [ ] Implemented clone
  - [ ] King rules 
    - [ ] Implemented one-step moves
    - [ ] Implemented castling
    - [ ] Implemented clone

## Javascript Front End (Current Progress)
- [ ] Design
  - [ ] Board Image 
  - [ ] Piece Images
  - [ ] Reserve Images
  - [ ] Player's Features
    - [ ] Perform moves
      - [ ] Drags pieces
      - [ ] Pawn promotion
      - [ ] Captures pieces displayed on reserve
      - [ ] Blocks illegal moves
    - [ ] Undo moves
- [ ] Chess Clock
  - [ ] Working timer
  - [ ] Timer reverts back after undo
- [ ] Chat Box

## AI (Later)
- Algorithms
  - [ ] Random AI
  - [ ] Minimax Algorithm
- AI Player
  - [ ] Two Players vs Team AI
  - [ ] Two Players vs AI and One Player

## Server (Later)
- [ ] Deploy to Heroku