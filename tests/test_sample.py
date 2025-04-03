import pytest
import allure


@allure.feature("Math Operations")
@allure.story("Addition")
def test_addition():
    allure.attach("Checking addition", name="Test Step", attachment_type=allure.attachment_type.TEXT)
    assert 2 + 3 == 5


@allure.feature("Math Operations")
@allure.story("Subtraction")
def test_subtraction():
    allure.attach("Checking subtraction", name="Test Step", attachment_type=allure.attachment_type.TEXT)
    assert 6 - 2 == 4


# @allure.feature("Math Operations")
# @allure.story("Multiplication")
# def test_multiplication():
#     allure.attach("Checking multiplication", name="Test Step", attachment_type=allure.attachment_type.TEXT)
#     assert 6 * 2 == 12  # Fixed wrong assertion
