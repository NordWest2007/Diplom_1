from praktikum.bun import Bun
import unittest


class TestBuns(unittest.TestCase):

    def test_get_name(self):
        name = 'black bun'
        price = 150
        bun = Bun(name, price)
        assert bun.get_name() == name

    def test_get_price(self):
        name = 'black bun'
        price = 150
        bun = Bun(name, price)
        assert bun.get_price() == price
