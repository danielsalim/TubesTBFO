def cykParser(output,cnfGrammar):
    num = len(output)

    # table init
    CYKtable = [[set([]) for i in range(num)] for j in range(num)]

    # filling the CYKtable
    for x in range(num):
        for variable in cnfGrammar.items():
                for terminal in variable[1]:
                    if len(terminal) == 1 and terminal[0] == output[x]:
                        CYKtable[x][x].add(variable[0])

    for z in range(2,num+1):
        for x in range (0,num-z+1):
            y = x+z-1
            for k in range (x,y):   
                for variable in cnfGrammar.items():
                    for production in variable[1] :
                        if len(production) == 2 :
                            if(production[0] in CYKtable[x][k]) and (production[1] in CYKtable[k+1][y]): 
                                CYKtable[x][y].add(variable[0])
    #print(table)
    #print(table[0][num-1])
    if "S0" in CYKtable[0][num-1] :
        print(CYKtable[0][num-1])
        print("Accepted Syntax!")
    else :
        print(CYKtable[0][num-1])
        print("Syntax Error")