import random

def placeValue():
    text = "What is the place value of"

    # Easy Place Value
    x = random.randint(0, 100000)
    y = x

    # Calculate how many digits within the number
    count=0
    while(x>0):
        count=count+1
        x=x//10
    print(y)
    
    place = random.randint(0, count - 1)
    g = place - 1
    print(place)
    number = str(y)
    print(number[g])
    print('What is the place value of ' + str(number[g]) + ' in ' + str(y))
    print(str(place))


    

placeValue()