def quickest_time(goats):
    times = []
    for goat in goats:
        times.append(goat['time_in_seconds'])
    lowest_time = min(times)
    index = times.index(lowest_time)
    return goats[index]['name']