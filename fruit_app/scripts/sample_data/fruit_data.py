import json
import os

def get():
    '''
    delishably.txt data scraped from:
    https://delishably.com/fruits/list-of-different-kinds-of-fruits
    '''
    file_path = os.path.join(os.path.dirname(__file__), 'delishably.txt')
    with open(file_path) as input_file:
        fruits = [line.rstrip('\n') for line in input_file]

    fruits = list(filter(lambda x: x != '—', fruits))

    # upper = list(map(lambda x: x.upper(), fruits))
    # print(upper)

    fruits.sort()
    fruits_json = json.dumps(fruits, indent = 2, separators=(',', ': '))
    # print(fruits_json)

    # with open('fruits.json', 'w') as output_file:
    #     output_file.write(fruits_json)

    return fruits_json
