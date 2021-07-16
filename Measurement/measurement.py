import random
import math
import csv

csv_file = open('measurement.csv', 'w+')
csv_writer = csv.writer(csv_file)            

def housePlan():
    for i in range(100):
        x = random.randint(1 , 10)
        y = random.randint(1, 10)
        z = random.randint(y , 20)
        areas = ['hall', 'living-room', 'kitchen']
        Names = ['John', 'Richard', 'Adam', 'Varun', 'Muhammad', 'Abdullah', 'Umar']
        Name = random.choice(Names)
        area = random.choice(areas)
        Question =  Name + ' is drawing a plan of his house. The scale is ' + str(x) + 'cm to ' + str(y) + 'm. The ' + area + ' is ' + str(z) + 'm long. How long is the ' + area + ' in cm? Remember to round to the nearest whole number!'
        Answer = round((y / x) * z)
        csv_writer.writerow([Question , Answer])  
        print(Question)
        print(Answer)

housePlan()