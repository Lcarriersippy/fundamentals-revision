import copy

def longest_name(names):
    names_deep_copy = copy.deepcopy(names)
    name_lengths = []
    for name in names_deep_copy:
        name['length'] = len(name['name'])
        name_lengths.append(name['length'])
    longest_num = max(name_lengths)
    index = name_lengths.index(longest_num)
    return names_deep_copy[index]['name']
