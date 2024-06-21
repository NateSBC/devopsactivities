"This program add the total number of an number contained in a string"

def count(sequence, item):
    "sequence = a series of numbers, item = a number to find in the sequence"
    total_numbers = 0
    for number in sequence:
        if number == item:
            total_numbers += 1
    return total_numbers
    