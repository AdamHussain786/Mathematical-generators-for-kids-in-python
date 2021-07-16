import random
import csv

shapes = ['triangle', 'square', 'rectangle', 'pentagon', 'hexagon', 'septagon', 'octogon', 'nonagon', 'decagon']

csv_file = open('perimeter.csv', 'w')
csv_writer = csv.writer(csv_file)                   
csv_writer.writerow(['Question', 'Answer']) 

def perimeter():
    x = random.randint(0, 8)
    length = random.randint(0, 20)

    print(length)
    if(shapes[x] == 'triangle'):
        Question = 'The length of one side of a ' + shapes[x] + ' is ' + str(length) + '. What is its perimeter?'
        print(Question)
        answer = length * 3
        print(answer)
        csv_writer.writerow([Question, answer])
    elif(shapes[x] == 'square'):
        Question = 'The length of one side of a ' + shapes[x] + ' is ' + str(length) + '. What is its perimeter?'
        print(Question)
        answer = length * 4
        print(answer)
        csv_writer.writerow([Question, answer])
    elif(shapes[x] == 'rectangle'):
        Question = 'The length of one side of a ' + shapes[x] + ' is ' + str(length) + '. What is its perimeter?'
        print(Question)
        answer = length * 4
        print(answer)
        csv_writer.writerow([Question, answer])
    elif(shapes[x] == 'pentagon'):
        Question = 'The length of one side of a ' + shapes[x] + ' is ' + str(length) + '. What is its perimeter?'
        print(Question)
        answer = length * 5
        print(answer)
        csv_writer.writerow([Question, answer])
    elif(shapes[x] == 'hexagon'):
        Question = 'The length of one side of a ' + shapes[x] + ' is ' + str(length) + '. What is its perimeter?'
        print(Question)
        answer = length * 6
        print(answer)
        csv_writer.writerow([Question, answer])
    elif(shapes[x] == 'septagon'):
        Question = 'The length of one side of a ' + shapes[x] + ' is ' + str(length) + '. What is its perimeter?'
        print(Question)
        answer = length * 7
        print(answer)
        csv_writer.writerow([Question, answer])
    elif(shapes[x] == 'octogon'):
        Question = 'The length of one side of a ' + shapes[x] + ' is ' + str(length) + '. What is its perimeter?'
        print(Question)
        answer = length * 8
        print(answer)
        csv_writer.writerow([Question, answer])
    elif(shapes[x] == 'nonagon'):
        Question = 'The length of one side of a ' + shapes[x] + ' is ' + str(length) + '. What is its perimeter?'
        print(Question)
        answer = length * 9
        print(answer)
        csv_writer.writerow([Question, answer])
    elif(shapes[x] == 'decagon'):
        Question = 'The length of one side of a ' + shapes[x] + ' is ' + str(length) + '. What is its perimeter?'
        print(Question)
        answer = length * 10
        print(answer)
        csv_writer.writerow([Question, answer])

    
perimeter()

csv_file.close()