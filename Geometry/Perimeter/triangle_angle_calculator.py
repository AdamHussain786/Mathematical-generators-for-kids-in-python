import random 
import csv

#!!!--- This is a paired question! Use the first then the second function ---!!!

csv_file = open('triangle_angle_calculator.csv', 'w+')
csv_writer = csv.writer(csv_file)                  


globa = 0
globb = 0
globc = 0

def three_numbers_to_n(bob, target):
    n = target - bob
    a = random.randrange(0, n+1)
    b = random.randrange(a, n+1) - a
    c = n - a - b
    return a, b, c

def triangle_find_c():
    # Find the third angle of a triangle
    bob = 6
    result = three_numbers_to_n(bob, 186)
    print(bob, result, sum(result) + bob)

    global globa 
    global globb 
    global globc 

    globa = result[0]
    globb = result[1]
    globc = result[2]

    Question  = 'The triangle shown has angles abcd. Angle a is ' + str(globa) + '° and angle b is ' + str(globa) + '°. What is the size of angle c?'
    Answer = globc
    csv_writer.writerow([Question , Answer])  

    print(Question)
    print(Answer)

def triangle_find_d():
    # Find the reflex angle around c
    bob = 6
    result = three_numbers_to_n(bob, 186)
    print(bob, result, sum(result) + bob)

    Question  = 'What is the size of angle d?'
    Answer = 360 - globc
    csv_writer.writerow([Question , Answer])  

    print(Question)
    print(Answer)
   

triangle_find_c()
triangle_find_d()

# However many question you want
for i in range(100):
    triangle_find_c()
    triangle_find_d()