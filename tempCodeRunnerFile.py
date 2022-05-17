num = eval(input())
for x in range(num):
    for y in range(x,num-1):
        print(" ",end='')
    for y in range(x):
        print("H",end='')
    for y in range(x+1):
        print("H",end='')
    print()