import CFGtoCNF
import cyk
import sys
import codeSplitter as splt

filename = input("Masukkan file yang ingin di periksa <file>.txt: ")
output = splt.codeSplitter(filename)
cnfGrammar = CFGtoCNF.convert()
cyk.cyk(output, cnfGrammar)