def compareTriplets(a, b):
    alice = 0;
    bob = 0;

    for i in range(len(a)):
        if a[i] > b[i]:
            alice+=1
        elif b[i] > a[i]:
            bob+=1
   
    return [alice, bob]


if __name__ == '__main__':
    a = [17, 28, 30,]
    b = [99, 16, 8]

    print(compareTriplets(a, b))

    a = [17, 28, 8,]
    b = [99, 16, 8]

    print(compareTriplets(a, b))