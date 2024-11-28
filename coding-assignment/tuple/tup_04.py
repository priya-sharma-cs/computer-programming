''' Find the frequency of each element in a tuple.'''
def element_frequency(tup):
    freq_dict = {}
    for element in tup:
        freq_dict[element] = freq_dict.get(element, 0) + 1
    return freq_dict

tup = (1, 2, 2, 3, 2, 4, 2)
frequency = element_frequency(tup)
print(frequency)
