## File 'wordifier.py'
def negate(word):
    return 'de' + word


def verb(word):
    return word + 'ize'


## File 'main.py'
def add_yes(word):
    return word + ', yes!'


print(dir())
# [..., 'add_yes']

from wordifier import *

print(dir())
# [..., 'add_yes', 'negate', 'verb']
