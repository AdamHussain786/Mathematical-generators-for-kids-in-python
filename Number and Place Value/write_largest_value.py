import random
import csv

csv_file = open('write_largest_value.csv', 'a')
csv_writer = csv.writer(csv_file)  

for i in range(2):
    x = [round(random.uniform(7, 9), 2), round(random.uniform(7, 9), 2),round(random.uniform(7, 9), 2),round(random.uniform(7, 9), 2),round(random.uniform(7, 9), 2)]
    largest_number = max(x)
    Question = 'Write the number with the largest value.' + str(x)
    Answer = largest_number
    csv_writer.writerow([Question , Answer])  
    
    print(x)
    print(largest_number)

csv_file.close()