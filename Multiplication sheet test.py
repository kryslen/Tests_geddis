def main():
    a,b,c,d=int(input()), int(input()), int(input()), int(input())
    print ('')
    for i in range (c, d+1):
        print('\t', i, end='') # adding row
    for i in range (a, b+1): #adding column
        print ('\n', i, end='')
        for j in range (c, d+1): #multiple
            print ('\t', i*j, end='')
