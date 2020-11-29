"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

telephones = set()

for call in calls:
    telephones.add(call[0])
    telephones.add(call[1])

for text in texts:
    telephones.add(text[0])
    telephones.add(text[1])

print('There are %i different telephone numbers in the records'%(len(telephones)))