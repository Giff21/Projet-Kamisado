def possible_move(dark: list, light: list, pawn: list, player: int) -> list:
    """gives the coordonates of every tiles the pawn can go

    Args:
        dark (list): darks pawn positions
        light (list): light pawns positions
        pawn (list): position of the pawn we have to play
        player (int): 0 (dark) or 1 (light)

    Returns:
        list: a list of all possible coordonates (list of lists)
    """

    pawn_row = pawn[0]
    pawn_column = pawn[1]
    towers_positions = dark + light
    possible_move = []

    # possible directions
    if player == 0:
        directions = [[-1, 0], [-1, 1], [-1, -1]]
    else:
        directions = [[1, 0], [1, -1], [1, 1]]

    # check possible tiles
    for dir_rows, dir_column in directions:
        currentRow = pawn_row + dir_rows
        currentColumn = pawn_column + dir_column

        while 0 <= currentRow < 8 and 0 <= currentColumn < 8:  # dimentions of the board
            if [currentRow, currentColumn] in towers_positions:
                break

            possible_move.append([currentRow, currentColumn])
            currentRow += dir_rows
            currentColumn += dir_column

    if not possible_move:
        return [pawn, pawn]

    return possible_move
