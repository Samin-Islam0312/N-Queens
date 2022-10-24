class Board():
  
    ##########################################
    ####   Constructor
    ##########################################
    def __init__(self, n):
        self.n = n
        self.spaces = n * n

        #indicates that all moves are possible at
        #the beginning
        self.constraints = [0 for i in range(self.spaces)]

        #holds the final places of the queens
        self.queenSpaces = []


    ##########################################
    ####   Move Functions
    ##########################################

    #returns all moves that have 0 constraints on them
    def getPossibleMoves(self):
        possibleMoves = []
        for move, numConstraints in enumerate(self.constraints):
            if numConstraints == 0:
                possibleMoves.append(move)
        return possibleMoves

    def makeMove(self, space):


        # add the queen
        self.queenSpaces.append(space)

        # add the conflicts
        self.addOrRemoveConstraints(space)


    def removeMove(self, space):

        #remove the queen
        self.queenSpaces.remove(space)

        #remove the dependent conflicts
        self.addOrRemoveConstraints(space, add=False)


    ##########################################
    ####   Constraint Logic
    ##########################################

    #adds or removes constraints along the row, col, and diags of a move
    def addOrRemoveConstraints(self, move, add=True):

        # choosing whether to use add or remove function
        if (add):
            mutationFx = self.addConstraint
        else:
            mutationFx = self.removeConstraint

        row = move // self.n
        col = move % self.n
        rdStartRow = row + col
        ldStartRow = row - col

        for i in range(self.n):

            #row
            mutationFx(self.rcToSpace(row, i))

            #col
            mutationFx(self.rcToSpace(i, col))

            # / diag
            if rdStartRow > -1:
                mutationFx(self.rcToSpace(rdStartRow, i))
                rdStartRow -= 1

            # \ diag
            if ldStartRow < self.n:
                mutationFx(self.rcToSpace(ldStartRow, i))
                ldStartRow += 1

    #add 1 to the constraint counter for a particular space
    def addConstraint(self, move):
        if not move == -1:
            self.constraints[move] += 1

    #remove 1 from the constraint counter for a particular space
    def removeConstraint(self, move):
        if not move == -1:
            self.constraints[move] -= 1

    ##########################################
    ####   Utility Functions
    ##########################################

    #returns the corresponding space # based on 0-indexed row and column
    #returns -1 if the space is not on the board
    # e.g.
    # rcToSpace(3,4) # the space at row 3, column 4
    # > 28           # the corresponding space number given an 8x8 board
    def rcToSpace(self, row, col):
        space = row * self.n + col
        if space >= self.spaces or space < 0:
            return -1
        else:
            return space


    def print(self):
        for r in range(self.n):
            row = ""
            for c in range(self.n):
                if(self.rcToSpace(r,c) in self.queenSpaces):
                    row += "Q"
                else:
                    row += "-"
                row += "  "
            print(row)

