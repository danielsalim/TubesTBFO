import CFGtoCNF
import cykParser as cyk
import sys
import codeSplitter as splt

cnfGrammar = CFGtoCNF.convert()
# print(cnfGrammar)

filename = sys.argv[1]
# masukin di terminal 'python main.py <file>.py
print("Compiling...")

output = splt.codeSplitter(filename)
cyk.cykParser(output,cnfGrammar)