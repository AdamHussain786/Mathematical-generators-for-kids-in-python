from random import randint
import csv
import numpy

csv_file = open('mean.csv', 'a')
csv_writer = csv.writer(csv_file)  

for i in range(10):
    Scores = [randint(1 , 20), randint(1 , 20), randint(1 , 20),
    randint(1 , 20), randint(1 , 20), randint(1 , 20), 
    randint(1 , 20), randint(1 , 20)]
    Question = 'Here are some scores from a test: ' + str(Scores) + '. Calculate the mean.'
    Answer = numpy.mean(Scores)
    csv_writer.writerow([Question , Answer])  
    print(Question)
    print(Answer)

csv_file.close()