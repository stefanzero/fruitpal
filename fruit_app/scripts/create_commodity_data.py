import sample_data.fruit_data as fruit_data
import sample_data.country_data as country_data
import random
import math

country_dict = country_data.get()
countries= country_dict.keys()
# print(countries)
fruits = fruit_data.get()
# print(fruits)

'''
Return a number with 2 decimal places of the specified power
'''
def get_random_value(power):
    a = 10**(power + 2)
    b = 10**(power + 3)
    c = 10**power
    decimal = random.randint(0, 99) / 100
    return math.floor(random.randint(a, b) / 100) + decimal

def random_countries(n):
    return random.sample(countries, n)

def random_fruits(n):
    return random.sample(fruits, n)


