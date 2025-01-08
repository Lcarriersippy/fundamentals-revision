def participants(goats):
    for goat in goats:
        del goat['time_in_seconds']
    return goats