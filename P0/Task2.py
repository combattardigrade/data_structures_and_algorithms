"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
longestTime = 0
index = 0
longestTimeIndex = 0

for call in calls:
    if int(call[3]) > longestTime:
        longestTime = int(call[3])
        longestTimeIndex = index
    index += 1

print('%s spent the longest time, %s seconds, on the phone during September 2016.' %(str(calls[longestTimeIndex][0]), str(calls[longestTimeIndex][3])))