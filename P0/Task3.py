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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def get_code(n):
  if n[0] == '(':
    code = '(' + n[n.find("(")+1:n.find(")")] + ')' 
  
  elif n[0] == '7' or n[0] == '8' or n[0] == '9':
    code = n[0] + n[1] + n[2] + n[3]
  
  elif (n[0] + n[1] + n[2]) == '140':
    code = n[0] + n[1] + n[2] + n[3]

  return code
  

def print_partA(codes):
  print('The numbers called by people in Bangalore have codes:')
  for code in sorted(codes):
    print(code)

def print_partB(codes_from, total_bangalore):
  r = total_bangalore / codes_from
  print('%s percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'%(str(round(r * 100,2) )))

def main():
  codes_from = dict()
  codes_to = dict()
  total_bangalore = 0

  for call in calls:
    code_from = get_code(call[0])
    code_to = get_code(call[1])

    if code_from == '(080)' and code_to == '(080)':
      total_bangalore += 1

    if code_to in codes_to:
      codes_to[code_to] += 1
    else:
      codes_to[code_to] = 1

    if code_from in codes_from:
      codes_from[code_from] += 1
    else:
      codes_from[code_from] = 1
  
  print_partA(codes_to)
  print_partB(codes_from['(080)'], total_bangalore)


main()