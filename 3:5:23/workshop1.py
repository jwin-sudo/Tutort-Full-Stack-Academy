def drawStar(size):
    star = 1
    start = size
    for i in range(0, size, 1):
        temp = star
        for k in range(0, size - i - 1, 1):
            print(" ", end='')
        for j in range(0, 2*size-1, 1):
            if(j >= start and temp > 0):
                print('* ', end='')
                temp = temp - 1

        star = star + 1
        start = start - 1
        print(' ')


drawStar(5)
