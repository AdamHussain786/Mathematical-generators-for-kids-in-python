import random
import csv

# x + int
# x - int
# Pick random questions to show the user for this one

csv_file = open('algebra.csv', 'a')
csv_writer = csv.writer(csv_file)                  
csv_writer.writerow(['Question', 'Answer'])

def algebraAdd():
  for i in range(1000):
    y = random.randint(1, 10)
    x = random.randint(1, 10)
    z = random.randint(1, 10)
    f = random.randint(1, 10)

 
    #Question
    Question = str(x) + "x + " + str(y) + " = " + str(z) + "x + " + str(f)

    if((z-x) == 0):
      print("/0 Error")
    else:
      # If it outcomes a whole number
      if(((y-f) / (z-x)).is_integer()):
        Answer = str((y-f) / (z-x))
        print(Question)
        print(Answer)
        csv_writer.writerow([Question , Answer])  
        
        
      

def algebraSubtract():
  for i in range(10):
    y = random.randint(1, 10)
    x = random.randint(1, 10)
    z = random.randint(1, 10)
    f = random.randint(1, 10)

    Question = str(x) + "x - " + str(y) + " = " + str(z) + "x - " + str(f)

    if((z-x) == 0):
      print("/0 Error")
      # Do not push to website

    elif(((f-y) / (z-x)).is_integer()):
      print(Question)
      print("x" + " = " + str((f-y) / (z-x)))
      #push to website


algebraAdd()
algebraSubtract()
csv_file.close()