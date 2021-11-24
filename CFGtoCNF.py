import itertools

left, right = 0, 1
K, V, Productions = [],[],[]
variablesJar = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z",
"A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", "O1", "P1", "Q1", "R1", "S1", "T1", "U1", "W1", "X1", "Y1", "Z1",
"A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "K2", "L2", "M2", "N2", "O2", "P2", "Q2", "R2", "S2", "T2", "U2", "W2", "X2", "Y2", "Z2",
"A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "K3", "L3", "M3", "N3", "O3", "P3", "Q3", "R3", "S3", "T3", "U3", "W3", "X3", "Y3", "Z3"]


def cleanProduction(expression):
	result = []
	rawRulse = expression.replace('\n','').split(';')
	for rule in rawRulse:
		leftSide = rule.split(' -> ')[0].replace(' ','')
		rightTerms = rule.split(' -> ')[1].split(' | ')
		for term in rightTerms:
			result.append( (leftSide, term.split(' ')) )
	return result


def splitFile(file):
	K = (file.split("Variables:\n")[0].replace("Terminals:\n","").replace("\n",""))
	V = (file.split("Variables:\n")[1].split("Productions:\n")[0].replace("Variables:\n","").replace("\n",""))
	P = (file.split("Productions:\n")[1])
	K = K.replace('  ',' ').split(' ')
	V = V.replace('  ',' ').split(' ')
	return K, V, cleanProduction(P)


def setupDict(productions, variables, terms):
	result = {}
	for production in productions:
		if production[left] in variables and production[right][0] in terms and len(production[right]) == 1:
			result[production[right][0]] = production[left]
	return result


def rewrite(target, production):
	result = []
	positions = [i for i,x in enumerate(production[right]) if x == target]
	for i in range(len(positions)+1):
 		for element in list(itertools.combinations(positions, i)):
 			tadan = [production[right][i] for i in range(len(production[right])) if i not in element]
 			if tadan != []:
 				result.append((production[left], tadan))
	return result


def isUnitary(rule, variables):
	if rule[left] in variables and rule[right][0] in variables and len(rule[right]) == 1:
		return True
	return False


def isSimple(rule):
	if rule[left] in V and rule[right][0] in K and len(rule[right]) == 1:
		return True
	return False


def newS(productions, variables): #Add S0->S rule
	variables.append('S0')
	return [('S0', [variables[0]])] + productions


def eliminateTerminalWithTerminal(productions, variables): #Remove rules like A->Bc and replaced  by A->BZ and Z->c
	newProductions = []
	dictionary = setupDict(productions, variables, terms=K)
	for production in productions:
		if isSimple(production):
			newProductions.append(production)
		else:
			for term in K:
				for index, value in enumerate(production[right]):
					if term == value and not term in dictionary:
						dictionary[term] = variablesJar.pop()
						V.append(dictionary[term])
						newProductions.append( (dictionary[term], [term]) )
						production[right][index] = dictionary[term]
					elif term == value:
						production[right][index] = dictionary[term]
			newProductions.append( (production[left], production[right]) )
	return newProductions


def eliminateNonUnitry(productions, variables): #Eliminate non unitry rules
	result = []
	for production in productions:
		k = len(production[right])
		if k <= 2:
			result.append( production )
		else:
			newVar = variablesJar.pop(0)
			variables.append(newVar+'1')
			result.append( (production[left], [production[right][0]]+[newVar+'1']) )
			i = 1
			for i in range(1, k-2 ):
				var, var2 = newVar+str(i), newVar+str(i+1)
				variables.append(var2)
				result.append( (var, [production[right][i], var2]) )
			result.append( (newVar+str(k-2), production[right][k-2:k]) ) 
	return result


def eleminateNonTerminal(productions): #Delete non terminal rules
	newSet = []
	outlaws, erased = [],[]
	for production in productions:
		if 'e' in production[right] and len(production[right]) == 1:
			outlaws.append(production[left])
		else:
			erased.append(production)
	production = erased
	for outlaw in outlaws:
		for production in productions + [e for e in newSet if e not in productions]:
			if outlaw in production[right]:
				newSet = newSet + [e for e in  rewrite(outlaw, production) if e not in newSet]
	return newSet + ([productions[i] for i in range(len(productions)) 
							if productions[i] not in newSet])


def unit_routine(rules, variables):
	unitaries, result = [], []
	for aRule in rules:
		if isUnitary(aRule, variables):
			unitaries.append( (aRule[left], aRule[right][0]) )
		else:
			result.append(aRule)
	for uni in unitaries:
		for rule in rules:
			if uni[right]==rule[left] and uni[left]!=rule[left]:
				result.append( (uni[left],rule[right]) )
	return result


def unit(productions, variables):
	i = 0
	result = unit_routine(productions, variables)
	tmp = unit_routine(result, variables)
	while result != tmp and i < 1000:
		result = unit_routine(tmp, variables)
		tmp = unit_routine(result, variables)
		i+=1
	return result

global CNF
CNF = {}

def convertToMap (Production):
	for i in range (len(Production)):
		s = ''
		for j in range (len(Production[i][1])):
			s = s + Production[i][1][j]
		CNF.update({s : Production[i][0]})

def convert ():
	try:
		file = open('grammar.txt').read()
		K, V, Productions = splitFile(file)
		for nonTerminal in V:
			if nonTerminal in variablesJar:
				variablesJar.remove(nonTerminal)
		Productions = newS(Productions, variables=V)
		Productions = eliminateTerminalWithTerminal(Productions, variables=V)
		Productions = eliminateNonUnitry(Productions, variables=V)
		Productions = eleminateNonTerminal(Productions)
		Productions = unit(Productions, variables=V)
		convertToMap(Productions)
		return CNF
	except:
		print("CFG grammar 'grammar.txt' not found")

Line = convert()