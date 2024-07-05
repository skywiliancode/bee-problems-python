A, B, C = input().split()

biggerAB = (int(A) + int(B) + abs(int(A) - int(B))) / 2
print('{} eh o maior'.format(int(biggerAB if biggerAB > int(C) else int(C))))
