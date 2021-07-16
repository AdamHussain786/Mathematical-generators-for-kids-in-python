import random
import csv

csv_file = open('identify_multiples_of _two_numbers.csv', 'a')
csv_writer = csv.writer(csv_file)                  

for i in range(1):
    multiples = [random.randint(2, 9), random.randint(2, 9)]
    x = random.choice(multiples) 
    y = random.choice(multiples) 

    if(x == y):
        x += random.randint(1,3)

    print(x, y)
    Option1 = [x * random.randint(2,10), x * random.randint(2,10), x * random.randint(2,10)]
    Option2 = [y * random.randint(2,10), y * random.randint(2,10), y * random.randint(2,10)]
    Option3 = [random.randint(2, 10) * random.randint(2, 10), random.randint(2, 10) * random.randint(2, 10), random.randint(2, 10) * random.randint(2, 10)]
    Option4 = [random.randint(2, 10) * random.randint(2, 10), random.randint(2, 10) * random.randint(2, 10), random.randint(2, 10) * random.randint(2, 10)]
    Option5 = [random.randint(2, 10) * random.randint(2, 10), random.randint(2, 10) * random.randint(2, 10), random.randint(2, 10) * random.randint(2, 10)]
    print(Option1)
    print(Option2)
    print(Option3)
    print(Option4)
    print(Option5)
    Question = 'Write down the group of numbers below that are all multiples of either ' + str(x) + ' or ' + str(y) + '.'
    print(Question)
    Answers = [str(Option1), str(Option2), str(Option3), str(Option4), str(Option5)]
    random.shuffle(Answers)
    csv_writer.writerow([Question , Answers])  
    
csv_file.close()