from array import *

def pasc(arr) :
    row = len(arr)
    col =len(arr[0])
    for i in range(row) :
            for j in range(col):
                if i > 0 :
                    arr[i][j] = arr[i-1][j]+arr[i][j-1]    
                                                      
n = int(input("n : "))
c = 1
arr = [[c]*n]*n

row = len(arr)
col =len(arr[0])
for i in range(row) :
            for j in range(col):
                arr[i][j] = 1

pasc(arr)

for r in arr :
    print(r)


