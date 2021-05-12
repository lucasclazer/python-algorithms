#first
# accessPosition [0][0]
# accessPosition [1][1]
# accessPosition [2][2]

#second
# accessPosition [0][2]
# accessPosition [1][1]
# accessPosition [2][0]

def diagonalDifference(arr):
    ans=0
    first=0
    second=0
    
    length = len(arr)
    for i in range(length):
        first += arr[i][i]
        second += arr[i][-1 * i + (length-1)]
    
    ans = first - second

    if ans > 0:    
        return ans
    elif ans < 0:    
        return -1*ans
    
    return 0
    
if __name__ == '__main__':
    arr = [[11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]]
    print(diagonalDifference(arr))



