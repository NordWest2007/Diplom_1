import unittest

from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger(unittest.TestCase):
    def test_set_buns(self):
        burger_name = 'roll'
        burger = Burger()
        burger.set_buns(burger_name)
        assert burger_name == burger.bun

    def test_add_ingredient(self):
        ingredient = 'cheese'
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        ingredients = ['cheese', 'onion']
        burger = Burger()
        burger.add_ingredient(ingredients[0])
        burger.add_ingredient(ingredients[1])
        burger.remove_ingredient(0)
        assert ingredients[1] in burger.ingredients
        assert len(burger.ingredients) == 1


if __name__ == '__main__':
    unittest.main()
