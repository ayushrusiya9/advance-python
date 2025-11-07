while True:
    res = int(input("1. For Addition \n2. For Subtraction \n3. For exit \nEnter : "))
    sum = 0
    if res == 1:
        l = int(input('How many values?\nEnter: '))
        for i in range(0,l):
            i = int(input('Enter Value : '))
            sum += i
        print(sum)
    elif res == 2:
        l = int(input('How many values?\nEnter: '))
        values = []
        for _ in range(0,l):
            val = int(input('Enter Value : '))
            values.append(val)
        result = values[0]
        for i in range(1,l):
            result = result - values[i]
        print(result)
    elif res == 3:
        break;
    else:
        print('Invalid Input')

        
            
            
