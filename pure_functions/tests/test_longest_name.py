import pytest
from pure_functions.utils.longest_name import longest_name

class TestLongestName():
    def test_returns_name(self):
        goat_data = [{'name': 'harley', 'time_in_seconds': 9}]
        assert longest_name(goat_data) == 'harley'

    def test_returns_longest_name(self):
        goat_data = [{'name': 'harley', 'time_in_seconds': 9}, {'name': 'flamingo', 'time_in_seconds': 15}]
        assert longest_name(goat_data) == 'flamingo'
