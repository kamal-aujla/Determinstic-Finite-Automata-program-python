from gen import ending
from starting_DFA import starting
from substring_DFA import substring

print("1. Ending with a string ")
print("2. Starting with a string ")#abc
print("3. Containing a substring ")
# input option
option = int(input("Choose a case:  "))

# case for ending with string
if option == 1:
    ending()

#case for starting with string
if option == 2:
    starting()

# case for substring
if option == 3:
    substring()