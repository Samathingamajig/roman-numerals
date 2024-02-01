from roman_numerals import roman_to_decimal, decimal_to_roman
from .romans_and_decimals import romans_and_decimals
import pytest


@pytest.mark.parametrize(
    ("roman, decimal"),
    romans_and_decimals,
)
def test_roman_to_decimal(roman, decimal):
    assert roman_to_decimal(roman) == decimal


@pytest.mark.parametrize(
    ("roman, decimal"),
    romans_and_decimals,
)
def test_decimal_to_roman(roman, decimal):
    assert decimal_to_roman(decimal) == roman
