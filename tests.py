from main import metod_dichotomy, func
import unittest

class TestTask3(unittest.TestCase):

    def setUp(self):
        self.regular = (0.25, 2)
        self.inf = (0, 2)
        self.up = (0.5, 2)
        self.low = (0.25, 0.5)
        self.dot = (0.5, 0.5)
        self.eps = 0.0000000001

    def test_regular(self): #обычный случай
        res = metod_dichotomy(func, self.regular[0], self.regular[1], self.eps)
        lower_eps = abs(0.5 - res[1][-1]) < self.eps
        self.assertEqual(lower_eps, True)

    def test_inf(self): #функция уходит в бесконечность
        res = metod_dichotomy(func, self.inf[0], self.inf[1], self.eps)
        lower_eps = abs(0.5 - res[1][-1]) < self.eps
        self.assertEqual(lower_eps, True)

    def test_low(self): #строго монотонно убывает
        res = metod_dichotomy(func, self.low[0], self.low[1], self.eps)
        lower_eps = abs(0.5 - res[1][-1]) < self.eps
        self.assertEqual(lower_eps, True)

    def test_up(self): #строго монотонно возрастает
        res = metod_dichotomy(func, self.up[0], self.up[1], self.eps)
        lower_eps = abs(0.5 - res[1][-1]) < self.eps
        self.assertEqual(lower_eps, True)

    def test_dot(self): #отрезок - это точка
        res = metod_dichotomy(func, self.dot[0], self.dot[1], self.eps)
        lower_eps = abs(0.5 - res[1][-1]) < self.eps
        self.assertEqual(lower_eps, True)
