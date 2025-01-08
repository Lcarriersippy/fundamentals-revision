import pytest
from pure_functions.utils.participants import participants

class TestParticipants():
    def test_participants_produces_list_with_dictionary(self):
        goats = [{'name': 'harley', 'time_in_seconds': 9}]
        assert participants(goats) == [{'name': 'harley'}]

    def test_participants_produces_list_with_multiple_dictionaries(self):
        goats = [{'name': 'harley', 'time_in_seconds': 9}, {'name': 'flamingo', 'time_in_seconds': 7}]
        assert participants(goats) == [{'name': 'harley'}, {'name': 'flamingo'}]
