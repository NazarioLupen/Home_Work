# HW2 TASK 2


number = int(input('Please digit four digits''\n'))
if number >= 1000 and number <= 9999:
    print('This is your number', number)
    res = [int(x) for x in str(number)] 
    print(res)
    print(res[0]*res[1]*res[2]*res[3])
    res.reverse()
    print(res)
    res.sort()
    print(res)
else:
    print('Please try again the number isn\'t 4 digit')
