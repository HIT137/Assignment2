from collections import Counter
import csv

with open (r'C:\Users\kzb19\Desktop\TEXT.txt') as input_file:
    count = Counter(word for line in input_file for word in line.split())

print(count.most_common(30))



