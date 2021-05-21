"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_turn = 0
    o_turn = 0
    if board == initial_state():
        x_turn += 1
        return X
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                x_turn += 1
            elif board[i][j] == "O":
                o_turn += 1
    if o_turn < x_turn:
        return O
    return X
    # elif o_turn < x_turn:
    #     o_turn += 1
    #     return O
    # else:
    #     x_turn += 1
    #     return X

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i, j))

    return actions_set
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid Action!")
    else:
        board_result = copy.deepcopy(board)
        board_result[action[0]][action[1]] = player(board)

    return board_result

    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check row
    for row in board:
        if len(set(row)) == 1 and row[0] != EMPTY:
            return row[0]

    # check column
    for i in range(3):
        column = [board[j][i] for j in range(3)]
        if len(set(column)) == 1 and column[0] != EMPTY:
            return column[0]

    # check diagonal
    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != EMPTY:
        return board[0][0]
    if len(set([board[i][2 - i] for i in range(3)])) == 1 and board[0][2] != EMPTY:
        return board[0][2]

    return None

    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True

    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            output = 1
        elif winner(board) == O:
            output = -1
        else:
            output = 0
        return output
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    alpha = -math.inf
    beta = math.inf

    if player(board) == X:
        action = max_helper(board, alpha, beta)[1]
    else:
        action = min_helper(board, alpha, beta)[1]
    return action
    # raise NotImplementedError


def max_helper(board, alpha, beta):
    """
    Check the action in actions that has the max value
    """
    val_max = -math.inf
    action_chosen = None
    if terminal(board):
        return utility(board), None
    for action in actions(board):
        val, action_plan = min_helper(result(board, action), alpha, beta)
        if val > val_max:
            val_max = val
            action_chosen = action
        if alpha >= beta:
            break

    return val_max, action_chosen


def min_helper(board, alpha, beta):
    """
    Check the action in actions that has the min value
    """
    val_min = math.inf
    action_chosen = None
    if terminal(board):
        return utility(board), None
    for action in actions(board):
        val, action_plan = max_helper(result(board, action), alpha, beta)
        if val < val_min:
            val_min = val
            action_chosen = action
        if alpha >= beta:
            break

    return val_min, action_chosen
