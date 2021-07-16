import random
import csv

csv_file = open('calculating_costs.csv', 'a')
csv_writer = csv.writer(csv_file)  

for i in range(100):
    Destinations = ['Holiday', 'Trip', 'Excursion', 'Family Trip']
    adultPrice = random.randint(100 , 400)
    childPrice = random.randint(100, 200)
    adultQuantity = random.randint(1, 5)
    childQuantity = random.randint(1, 5)

    Question = 'A ' + random.choice(Destinations) + ' costs £' + str(adultPrice) + ' for an adult.' + ' It is £' + str(childPrice) + ' less for a child.' + ' How much is it for ' + str(adultQuantity) + ' adults and ' + str(childQuantity) + ' children to go?'
    Answer = ((adultPrice * adultQuantity) + ((adultPrice - childPrice )* childQuantity))
    csv_writer.writerow([Question , Answer])  
    print(Question)
    print(Answer)
    
csv_file.close()