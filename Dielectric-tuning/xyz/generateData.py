import os
import generateFiles as gen
import splineplot as spl

Path = gen.path

def readtxt():
    nameDict = {}
    for txt in os.listdir(Path):
	if ".txt" in txt:
	    lines = open(txt, 'r').read()
	    txt = str(txt[:-4])
	    nameDict.update({txt : lines})
    return nameDict

def getline(line, linenum):
    block = line[linenum].split("\n")
    if spl.can_float(block[-2].strip()):
	return float(block[-2].strip())

def findVIE():
    nameDict = readtxt()
    dataDict = {}
    errorList = []
    for name in nameDict:
	rFile = nameDict[name]
	if "ERROR" in rFile:
	    errorList.append(name)
	    continue
        lines = rFile.split("0.0\n")
	BLYP_80 = round(getline(lines, 0), 10) * 23.061
	HF_80 = round(getline(lines, 1), 10) * 23.061
	B3LYP_80 = round(getline(lines, 2), 10) * 23.061
        BHHLYP_80 = round(getline(lines, 3), 10) * 23.061
	dataDict.update({name+"_80" : [BLYP_80, B3LYP_80, BHHLYP_80, HF_80]})
        BLYP_1 = round(getline(lines, 4), 10) * 23.061
        HF_1 = round(getline(lines, 5), 10) * 23.061
        B3LYP_1 = round(getline(lines, 6), 10) * 23.061
	BHHLYP_1 = round(getline(lines, 7), 10) * 23.061
	dataDict.update({name+"_1" : [BLYP_1, B3LYP_1, BHHLYP_1, HF_1]})
        BLYP_opt = round(getline(lines, -5), 10) * 23.061
	HF_opt = round(getline(lines, -4), 10) * 23.061
	B3LYP_opt = round(getline(lines, -3), 10) * 23.061
	BHHLYP_opt = round(getline(lines, -2), 10) * 23.061
	dataDict.update({name+"_opt" : [BLYP_opt, B3LYP_opt, BHHLYP_opt, HF_opt]})
    return (dataDict, errorList)

def findHOMO(filename):
    nameDict = readtxt()
    rFile = nameDict[filename]

def gen_output():
    dataDict = findVIE()[0]
    nameDict = readtxt()
    errorList = findVIE()[1]
    print "errorlist: " + str(errorList)
    checkList = []
    for name in nameDict:
	if name in errorList:
	    checkList.append(name)
    for name in checkList:
	if name in nameDict:
	    del nameDict[name]
    finDict = {}
    for a in dataDict:
	newline = str(dataDict[a]).translate(None, "[]'")
	finDict.update({a : newline})
    data_file = open('VIE_data.csv', 'w')
    data_file.write('Species Name, BLYP_80, B3LYP_80, BHHLYP_80, HF_80, BLYP_1, B3LYP_1, BHHLYP_1, HF_1, BLYP_opt, B3LYP_opt, BHHLYP_opt, HF_opt, \n')
    for name in nameDict:
	data_file.write('%s, %s, %s, %s, \n' % (name, finDict[name+'_80'], finDict[name+'_1'], finDict[name+'_opt']) )
    error_file = open('ERROR_data.csv', 'w')
    error_file.write('List of Chemical Species in Which Convergence Failure Occured: , \n')
    for name in errorList:
        error_file.write('%s \n' % name)
    return finDict

dict = gen_output()
print dict
