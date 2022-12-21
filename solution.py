
def countVowelStrings(n: int) -> int:
    table =[]
    for i in range(n):
        list1=[]
        for j in range(6):
            list1.append(0)
        table.append(list1)
    print(table)
    for i in range(n):
        suma=0
        for j in range(6):
            if i==0 and j!=5:
                table[i][j]=1
            else:
                if j==0:
                    table[i][j]=table[i-1][5]
                elif j!=5:
                    table[i][j]=table[i][j-1]-table[i-1][j-1]
        suma = sum(table[i])
        print(suma)
        table[i][5] = suma
    print(table)
    return table[n-1][5]

print(countVowelStrings(4))
