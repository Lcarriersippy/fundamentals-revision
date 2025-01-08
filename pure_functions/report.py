from pure_functions.utils.longest_name import longest_name
from pure_functions.utils.quickest_time import quickest_time
from pure_functions.utils.participants import participants

def report(goat_results):
    longest_name_goat = longest_name(goat_results)
    quickest_time_goat = quickest_time(goat_results)
    participant_list = participants(goat_results)
    return {'longest_name': longest_name_goat, 'fastest_goat': quickest_time_goat, 'participants': participant_list}