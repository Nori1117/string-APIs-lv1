#write a python function, remove_duplicates() 
#which accepts a string and removes all duplicate characters from the given string and return its.

def remove_duplicates(value):
uniqs = ""
for x in value:
if not(x in uniqs):
uniqs+=x
return = uniqs
print(remove_duplicates("112233445566$$%%&&"))

#another solution 
from collections import OrderedDict
def removeDup(string):
    return ''.join(OrderedDict.fromkeys(string))
print removeDup("apple")

