import json

def alphabetize(names):
    """Alphabetizes the names in the given list"""

    alphabetized_list = []

    for name in names:
        if alphabetized_list:
            for i in alphabetized_list:
                # If name goes before i, insert name
                if name < i:
                    alphabetized_list.insert(alphabetized_list.index(i), name)
                    break
                # At end of alphabetized list, add name to end
                if alphabetized_list[-1] == i:
                    alphabetized_list.append(name)
                    break
        else:
            alphabetized_list.append(name)

    return alphabetized_list

def alphabetical_value(name):
    """Returns the alphabetical value of a name. a=1, b=2, c=3, etc
    For example: Colin is worth 3 + 15 + 12 + 9 + 14 = 53. """
    value = 0
    for char in name:
        value += ord(char)-64
    return value


with open('names.json') as names_file:
    names = json.load(names_file)

alphabetized = alphabetize(names)
total = 0

for name in alphabetized:
    index = alphabetized.index(name) + 1
    score = index * alphabetical_value(name)
    total += score

print(total)