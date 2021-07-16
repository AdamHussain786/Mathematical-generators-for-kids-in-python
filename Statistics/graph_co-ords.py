from matplotlib import interactive 
from matplotlib import pyplot as plt
import random
import numpy as np
import csv

csv_file = open('graph_co-ords.csv', 'a')
csv_writer = csv.writer(csv_file)                  

interactive(True)
def graph_coords():
    plt.grid()

    x = [*np.random.randint(7, size = 1)]
    y = [*np.random.randint(7, size = 1)]

    h = [*np.random.randint(7, size = 1)]
    j = [*np.random.randint(7, size = 1)]

    z = [*np.random.randint(7, size = 1)]
    a = [*np.random.randint(7, size = 1)]

    l = [*np.random.randint(7, size = 1)]
    k = [*np.random.randint(7, size = 1)]

    plt.scatter(x, y)
    plt.scatter(h, j)
    plt.scatter(z, a)
    plt.scatter(l, k)

    plt.text(x[0], y[0], '  House')
    plt.text(h[0], j[0], '  Library')
    plt.text(z[0], a[0], '  Supermarket')
    plt.text(l[0], k[0], '  Gym')

    Question1 = 'Write the co-ordinates of the House.'
    Question2 = 'Write the co-ordinates of the Library.'
    Question3 = 'Write the co-ordinates of the Supermarket.'
    Question4 = 'Write the co-ordinates of the Gym.'

    Answer1 = str(x[0]) + ',' + str(y[0])
    Answer2 = str(h[0]) + ',' +str(j[0])
    Answer3 = str(z[0]) + ',' +str(a[0])
    Answer4 = str(l[0]) + ',' +str(k[0])

    print(Question1)
    print(Question2)
    print(Question3)
    print(Question4)

    print(Answer1)
    print(Answer2)
    print(Answer3)
    print(Answer4)



    plt.xlabel('x')
    plt.ylabel('y')
    csv_writer.writerow([Question1 , Answer1])  
    csv_writer.writerow([Question2 , Answer2])  
    csv_writer.writerow([Question3 , Answer3])  
    csv_writer.writerow([Question4 , Answer4])  
    plt.savefig('img.png')
    input("return")
    
    

graph_coords()