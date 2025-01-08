import pytest
from pure_functions.utils.quickest_time import quickest_time

class TestQuickestTime():
    def test_quickest_time_selects_quickest_time(self):
        goats = [{'name': 'harley', 'time_in_seconds': 9}]
        assert quickest_time(goats) == 'harley'

    def test_quickest_time_selects_quickest_time_out_of_multiple(self):
        goats = [{'name': 'harley', 'time_in_seconds': 9}, {'name': 'flamingo', 'time_in_seconds': 7}]
        assert quickest_time(goats) == 'flamingo'

    def test_quickest_time_does_not_mutate_data(self):
        goats = [{'name': 'harley', 'time_in_seconds': 9}, {'name': 'flamingo', 'time_in_seconds': 7}]
        goats_copy = [{'name': 'harley', 'time_in_seconds': 9}, {'name': 'flamingo', 'time_in_seconds': 7}]
        quickest_time(goats)
        assert goats == goats_copy