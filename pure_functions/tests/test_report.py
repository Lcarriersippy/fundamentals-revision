import pytest
from pure_functions.report import report

class TestReport():
    def test_report_produces_a_report(self):
        goats = [{'name': 'harley', 'time_in_seconds': 9}]
        assert report(goats) == {'longest_name': 'harley', 'fastest_goat': 'harley', 'participants': [{'name': 'harley'}]}

    def test_report_produces_a_report_from_multiple_goats(self):
        goats = [{'name': 'harley', 'time_in_seconds': 9}, {'name': 'flamingo', 'time_in_seconds': 15}]
        assert report(goats) == {'longest_name': 'flamingo', 'fastest_goat': 'harley', 'participants': [{'name': 'harley'}, {'name': 'flamingo'}]}

    def test_ignore_average_goats(self):
        goats = [{'name': 'harley', 'time_in_seconds': 9}, {'name': 'hobarthobart', 'time_in_seconds': 11}, {'name': 'flamingo', 'time_in_seconds': 15}]
        assert report(goats) == {'longest_name': 'hobarthobart', 'fastest_goat': 'harley', 'participants': [{'name': 'harley'}, {'name': 'hobarthobart'}, {'name': 'flamingo'}]}
