"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload
from sample_players import *
from game_agent import *


class IsolationMinimaxTest(unittest.TestCase):
    """Unit tests for Minimax agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = RandomPlayer()
        self.player2 = MinimaxPlayer(search_depth=3, score_fn=open_move_score)
        self.game = isolation.Board(self.player1, self.player2, width=9, height=9)

    def testMiniMax(self):
        print(self.game.to_string())
        winner, history, outcome = self.game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(self.game.to_string())
        print("Move history:\n{!s}".format(history))


class IsolationAlphaBetaTest(unittest.TestCase):
    """Unit tests for AlphaBeta agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = AlphaBetaPlayer(search_depth=3, score_fn=open_move_score)
        self.player2 = RandomPlayer()
        self.game = isolation.Board(self.player1, self.player2, width=9, height=9)

    def testAlphaBeta(self):
        print(self.game.to_string())
        winner, history, outcome = self.game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(self.game.to_string())
        print("Move history:\n{!s}".format(history))


if __name__ == '__main__':
    unittest.main()
