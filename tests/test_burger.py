import pytest
import allure

from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient
from Diplom_1.burger import Burger


class TestBurger:

    @allure.title("Тест на установку булочки")
    def test_set_bun(self, bun_fixture):
        burger = Burger()
        burger.set_buns(bun_fixture)
        assert burger.bun == bun_fixture

    @allure.title("Тест на добавление ингредиента")
    def test_add_ingredient(self, burger_fixture, ingredient_fixture):
        assert len(burger_fixture.ingredients) == 1
        burger_fixture.add_ingredient(ingredient_fixture)
        assert len(burger_fixture.ingredients) == 2

    @allure.title("Тест на удаление ингредиента")
    def test_remove_ingredient(self, burger_fixture):
        burger_fixture.remove_ingredient(0)
        assert len(burger_fixture.ingredients) == 0

    @allure.title("Тест на перемещение ингредиента")
    def test_move_ingredient(self, burger_fixture):
        new_ingredient = Ingredient(ingredient_type="Соусы", name="Кетчуп", price=20)
        burger_fixture.add_ingredient(new_ingredient)

        burger_fixture.move_ingredient(0, 1)
        assert burger_fixture.ingredients[0].get_name() == "Кетчуп"
        assert burger_fixture.ingredients[1].get_name() == "Биокотлета"

    @allure.title("Тест на расчет цены бургера")
    @pytest.mark.parametrize("bun_price, ingredient_price, expected_price", [
        (50, 150, 250),
        (30, 100, 160),
        (10, 50, 70)
    ])
    def test_get_price(self, bun_price, ingredient_price, expected_price):

        bun = Bun(name="Test Bun", price=bun_price)
        ingredient = Ingredient(ingredient_type="Начинка", name="Test Ingredient", price=ingredient_price)

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_price() == expected_price

    @allure.title("Тест на создание чека")
    def test_get_receipt(self, burger_fixture):
        receipt = burger_fixture.get_receipt()
        assert "(==== Classic Bun ====)" in receipt
        assert "= начинки Биокотлета =" in receipt
        assert "(==== Classic Bun ====)\n" in receipt
        assert "Price: 698" in receipt