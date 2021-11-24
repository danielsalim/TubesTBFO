def cyk(output,cnfGrammar):
    num = len(output)
    table = [[set([]) for i in range(num)] for j in range(num)]

    for i in range(num):
        for var in cnfGrammar.items():
                for termin in var[1]:
                    if len(termin) == 1 and termin[0] == output[i]:
                        table[i][i].add(var[0])

    for l in range(2,num+1):
        for i in range (0,num-l+1):
            j = i+l-1
            for k in range (i,j):
                for var in cnfGrammar.items():
                    for prod in var[1] :
                        if len(prod) == 2 :
                            if(prod[0] in table[i][k]) and (prod[1] in table[k+1][j]):
                                table[i][j].add(var[0])
    # print(table)
    # print(table[0][n-1])
    if "S" in table[0][num-1] :
        print("Accepted Syntax!")
        #return True
    else :
        print("Syntax Error")
        #return False