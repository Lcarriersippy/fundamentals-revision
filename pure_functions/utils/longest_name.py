def longest_name(names):
    name_lengths = []
    for name in names:
        name['length'] = len(name['name'])
        name_lengths.append(name['length'])
    longest_num = max(name_lengths)
    index = name_lengths.index(longest_num)
    return names[index]['name']
