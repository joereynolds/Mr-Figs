import unittest
from src.bomb import Bomb

class TestChecker(unittest.TestCase):

    def test_check_is_instantiable(self):
        self.assertEqual(2, 2)

    def test_our_bomb_explodes_when_the_lifespan_is_zero(self):
        pass

if __name__ == '__main__':
    unittest.main()
