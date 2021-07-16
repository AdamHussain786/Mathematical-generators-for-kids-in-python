from random import randint
import random
import csv

csv_file = open('ratio.csv', 'a')
csv_writer = csv.writer(csv_file)  

for i in range(10):
    x = randint(2,9)
    ratio = [x * randint(1, 9), x * randint(1, 9)]

    min = ratio[0]
    if ratio[1] < ratio[0]:
        min = ratio[1]

    for i in range(1, min + 1):
        if((ratio[0] % i) == 0 and (ratio[1] % i) == 0):
            hcf = i

    new_ratio = [ratio[0] / hcf, ratio[1] / hcf]
    questionRatio = str(ratio[0]).strip('.0') + ':' + str(ratio[1]).strip('.0')
    Answer = str(new_ratio[0]).strip('.0') + ':'+ str(new_ratio[1]).strip('.0')
    Options = [str(randint(2, 20)) + ':' + str(randint(2, 20)),str(randint(2, 20)) + ':' + str(randint(2, 20)),str(randint(2, 20)) + ':' + str(randint(2, 20)),str(randint(2, 20)) + ':' + str(randint(2, 20)), Answer]
    random.shuffle(Options)
    Question = 'Which ratio is the equivalent to '  +  questionRatio + '? Write the correct answer.' + str(Options)
    csv_writer.writerow([Question , Answer])  

    #Debugging
    print(Question)
    print(Options)
    print(Answer)

csv_file.close()

#print('HCF is: ' + str(hcf))
#print('new ratio is: ' + str(new_ratio[0]).strip('.0') + ':' + str(new_ratio[1]).strip('.0'))
