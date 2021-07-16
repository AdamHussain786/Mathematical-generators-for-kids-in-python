import random
import math
import csv

fruits = ['apples', 'pears', 'raspberries', 'guavas', 'cherries']

csv_file = open('division.csv', 'a')
csv_writer = csv.writer(csv_file)                  


def divisionQuestions(iterations):
    for i in range(iterations):
        x = random.randint(0 , 4)
        y = random.randint(1 , 15)
        z = random.randint(15, 200)
        Question = 'If you need ' + str(y) + ' ' + fruits[x] + ' to make a tart, how many can be made with ' +  str(z) + ' ' + fruits[x] + '?'
        Answer = math.floor(z / y)
        csv_writer.writerow([Question , Answer])  

        #Debugging
        print(Question)
        print(Answer)

divisionQuestions(100)