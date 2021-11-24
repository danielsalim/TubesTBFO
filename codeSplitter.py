import re

def codeSplitter(inputFile):
    f = open(inputFile, "r")
    contents = f.read()
    output = re.split(r'\s+', contents)
    f.close()

    operators = ['=', '!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', r'\+', r'\*', r'\*\*', r'\'', r'\"', r'\'\'\'', r'\(', r'\)', 'none', 'not', 'true', 'false', r'\{', r'\}', r'\[', r'\]', 'for', '#', 'elif', 'else', 'while', 'break', 'continue', 'pass', 'def', 'return', 'range', 'raise', 'class', 'from', 'import', 'with', 'open', 'print']
    
    # Split the string for each operator and statement
    for opr in operators:
        tempResult = []
        for statement in output:
            x = re.split(r'[A..z]*(' + opr + r')[A..z]*', statement)
            
            for splittedx in x:
                tempResult.append(splittedx) 
        output = tempResult

    # Remove space from output
    for statement in output:
        if statement == '':
            output.remove(statement)

    # Split the variables
    tempResult = []
    for statement in output:
        if statement in operators:
            tempResult.append(statement)
        else:
            if statement == 'as' or statement == 'is' or statement == 'or' or statement == 'in' or statement == 'if' or statement == 'and':
                tempResult.append(statement)
            else:
                split = list(statement)
                tempResult.extend(split)
            
    return tempResult