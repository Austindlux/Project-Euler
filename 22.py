import json

with open('names.json') as names_file:
    names = json.load(names_file)

def alphabetize(names):
    """Alphabetizes the names in the given list"""
    print(names)
    alphabetized_list = []
    for name in names:
        print(alphabetized_list)
        if alphabetized_list:
            for i in alphabetized_list:
                if name < i:
                    print(1)
                    alphabetized_list.insert(alphabetized_list.index(i)-1, name)
                else:
                    print(1)
                    alphabetized_list.append(name)
        else:
            alphabetized_list.append(name)
    return alphabetized_list

list1 = ['austin', 'baloney', 'zucinni', 'anthem', 'qwerty', 'box', 'train', 'z']

print(alphabetize(list1))
