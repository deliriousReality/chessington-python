"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        moves = []
        if self.player == Player.WHITE:
            candidate_move = Square.at((current_square.row)+1,current_square.col)
            if board.get_piece(candidate_move) is None:
                moves.append(candidate_move)
            if current_square.row == 1:
                special_case_candidate_move = Square.at((current_square.row)+2,current_square.col)
                if board.get_piece(special_case_candidate_move) is None and board.get_piece(candidate_move) is None:
                    moves.append(special_case_candidate_move)
        else:
            candidate_move = Square.at((current_square.row)-1,current_square.col)
            if board.get_piece(candidate_move) is None:
                moves.append(candidate_move)
            if current_square.row == 6:
                special_case_candidate_move = Square.at((current_square.row)-2,current_square.col)
                if board.get_piece(special_case_candidate_move) is None and board.get_piece(candidate_move) is None:
                    moves.append(special_case_candidate_move)         
        return moves

    def square_occupied(candidate_move,moves,board):
        if board.get_piece(candidate_move) is None:
                moves.append(candidate_move)
        return moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []