import board

# board to be manipulated below
b = board.Board(8)

#returns true if there exists a potential queen placement given the current board state
#   and leaves b.queenspaces filled with the appropriate queen placements
#false if otherwise


def placeMoves():

    for move in b.getPossibleMoves():

        b.makeMove(move)

        if len(b.queenSpaces) == b.n:
            return True
        else:

            retVal = placeMoves()

            if retVal:
                return True

            else:
                b.removeMove(move)

    return False


#Hint 1: This should be recursively defined
#Hint 2: You should only need to use the following three functions from the board class
# - getPossibleMoves
# - makeMove
# - removeMove


if __name__ == "__main__":
    placeMoves()
    b.print()
