import random
import csv


csv_file = open('triangle_angle_calculator.csv', 'w+')
csv_writer = csv.writer(csv_file) 

def reverseQuestion():
    for i in range(100):
        Names = ['John', 'Richard', 'Adam', 'Varun', 'Muhammad', 'Abdullah', 'Umar']
        x = random.randint(0, 100)
        y = random.randint(1, 30)
        z = (x/2) + y
        Name = random.choice(Names)
        Question =  Name + ' thought of an integer. He halved it, then added ' + str(y) + '. The result was ' + str(z) + '. What integer did ' + Name + ' think of?'
        Answer = x
        print(Question)
        print(Answer)
        csv_writer.writerow([Question , Answer])  

reverseQuestion()