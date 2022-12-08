import chess

# create a chess board
board = chess.Board()

# create two chess bots
bot1 = chess.uci.popen_engine("/path/to/first/bot")
bot2 = chess.uci.popen_engine("/path/to/second/bot")

# have the bots play each other
while not board.is_game_over():
    # have the first bot make a move that will result in a stalemate
    result1 = bot1.play(board, chess.engine.Limit(time=0.1))
    move1 = result1.move
    if move1.uci() == "a1a8" or move1.uci() == "h1h8":
        board.push(move1)
        break
    # have the second bot make a move that will result in a stalemate
    result2 = bot2.play(board, chess.engine.Limit(time=0.1))
    move2 = result2.move
    if move2.uci() == "a1a8" or move2.uci() == "h1h8":
        board.push(move2)
        break
    # if the bots didn't make a move that results in a stalemate,
    # make a random move to keep the game going
    board.push(board.random_legal_move())

# print the result of the game
print(board.result())

# close the bots
bot1.quit()
bot2.quit()
