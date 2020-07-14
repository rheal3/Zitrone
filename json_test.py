# import json
#
# ingredients = {'carrot': ['deviled egg', 'cashew recipe']}
#
# json = json.dumps(ingredients)
# file = open('ingredients.json', 'w')
# file.write(json)
# file.close()
#
# with open('ingredients.json') as open_file:
#     my_list = [json.loads(line) for line in open_file]
#
# print(my_list)


import json
import os

def append_record(record):
    with open('my_file', 'a') as f:
        json.dump(record, f)
        f.write(os.linesep)

# demonstrate a program writing multiple records
# for i in range(10):
#     my_dict = {'number':i}
#     append_record(my_dict)

with open('my_file') as f:
    my_list = [json.loads(line) for line in f]

# ingredients = {'carrot': ['dump']}
# append_record(ingredients)
new_dict = {}

with open('my_file') as f:
    my_list = [json.loads(line) for line in f]
    for line in my_list:
        for key, value in line.items():
            if key not in new_dict:
                new_dict[key] = value
            else:
                new_dict[key] += value

print(new_dict)

            # if key == 'carrot':
            #     print(line[key])
            #     if


# print(my_list)
