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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def possible_telemarketers(numbers):
    print("These numbers could be telemarketers: ")    
    for n in sorted(numbers):
        if(numbers[n]['outgoing_calls'] > 0 and numbers[n]['outgoing_text'] == 0 and numbers[n]['incoming_text'] == 0 and numbers[n]['incoming_calls'] == 0):
            print(n)


def main():

    numbers = dict()
    
    for call in calls:
        outgoing_n = call[0]
        incoming_n = call[1]

        if outgoing_n not in numbers:
            numbers[outgoing_n] = {'outgoing_calls': 0, 'incoming_calls': 0, 'outgoing_text': 0, 'incoming_text': 0}
        
        if incoming_n not in numbers:
            numbers[incoming_n] = {'outgoing_calls': 0, 'incoming_calls': 0, 'outgoing_text': 0, 'incoming_text': 0}
        
        numbers[outgoing_n]['outgoing_calls'] += 1
        numbers[incoming_n]['incoming_calls'] += 1
        

    for text in texts:
        outgoing_t = text[0]
        incoming_t = text[1]

        if outgoing_t not in numbers:
            numbers[outgoing_t] = {'outgoing_calls': 0, 'incoming_calls': 0, 'outgoing_text': 0, 'incoming_text': 0}
        
        if incoming_t not in numbers:
            numbers[incoming_t] = {'outgoing_calls': 0, 'incoming_calls': 0, 'outgoing_text': 0, 'incoming_text': 0}
        
        numbers[outgoing_t]['outgoing_text'] += 1
        numbers[incoming_t]['incoming_text'] += 1
      
            
    possible_telemarketers(numbers)

main()