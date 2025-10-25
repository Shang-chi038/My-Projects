#FizzBuzz
""" #Using a for loop
for i in range(1,101):
    if (i%3 == 0) and (i%5 == 0):
        print('FizzBuzz')
        continue

    elif (i%3 == 0):
        print('Fizz')
        continue

    elif (i%5 == 0):
        print('Buzz')
        continue
    
    else:
        print(f'{i}')
        continue
 
"""

#Using a while loop
i = 0
while i < 100:
        i += 1
        #I declared my counter variable as zero and put the increment of my counter variable b4 the conditions, so that
            #if a 'continue' function is executed, our counter variable will still increase, till it reaches 100
        if (i%3 == 0) and (i%5 == 0):
            print('FizzBuzz')
            continue

        elif (i%3 == 0):
            print('Fizz')
            continue

        elif (i%5 == 0):
            print('Buzz')
            continue

        else:
            print(f'{i}')
