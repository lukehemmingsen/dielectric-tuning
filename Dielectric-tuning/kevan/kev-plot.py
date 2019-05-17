import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from scipy import integrate
import generateFiles as gen
import os
import splineplot as spl
import time
import datetime

NAME = "kev"
path = gen.path
X = spl.X

#makes it look pretty -> preferences/publication
font = {'weight' : 'bold' ,
        'size'   : 24}
plt.rc('font', **font)
fig = plt.figure()

def new_files(con, HFcon, B3con, BHHcon, filename):
    nm = filename
    gen.clear(nm)
    gen.generate_ins(con, HFcon, B3con, BHHcon, nm)
    os.system("qchem " + nm + "0.in > " + nm + ".out")
    os.system("qchem " + nm + "a1.in > " + nm + "a.out")
    os.system("qchem " + nm + "HF0.in > " + nm + "HF.out")
    os.system("qchem " + nm + "HFa1.in > " + nm + "HFa.out")
    os.system("qchem " + nm + "B3LYP0.in > " + nm + "B3LYP.out")
    os.system("qchem " + nm + "B3LYPa1.in > " + nm + "B3LYPa.out")
    os.system("qchem " + nm + "BHHLYP0.in > " + nm + "BHHLYP.out")
    os.system("qchem " + nm + "BHHLYPa1.in > " + nm + "BHHLYPa.out")

def sub_wait(filename):
    #print "Queued at " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    hasPath =  os.path.exists(path + "/" + filename + "BHHLYPa.out")
    somethingIsWrong = 0
    while not hasPath:
	time.sleep(1)
	hasPath = os.path.exists(path + "/" + filename + "BHHLYPa.out")
	somethingIsWrong += 1
	if somethingIsWrong > 900 :
	    return False
    time.sleep(10)
    #print "Waited %i seconds." % somethingIsWrong
    return True

def generate(con, HFcon, B3con, BHHcon, filename):
    new_files(con,HFcon,B3con,BHHcon,filename)
    if not sub_wait(filename) :
        print "Exceeded 15 minutes sleep."
        raise RuntimeError("Super computer did not execute within 15 minutes.")
    else :
        print "Files generated successfully."
        return filename

class GraphVals:

    def __init__(self, Filename):
	print Filename
	_anion = spl.get_anion(Filename)
	print _anion
	_neutral = spl.get_neutral(Filename)
	print _neutral	
	self.q = spl.charge_transfer(X, _anion[0], _anion[1], _neutral[0], _neutral[1])
	self.diffi = integrate.quad(spl.transfer_diffi, 0, 1, args=(_anion[0], _anion[1], _neutral[0], _neutral[1]))[0]
	print "Graphing" + Filename

    def newPara(self, other, mynum, myother):
	if self.diffi > 0 and other.diffi < 0:
	    return round((mynum + myother) / 2, 2)
	if self.diffi < 0 and other.diffi > 0:
	    return round((mynum + myother) / 2, 2)
	if self.diffi < 0 and other.diffi < 0:
	    if self.diffi >= other.diffi:
		return mynum
	    elif self.diffi < other.diffi:
		return myother
	if self.diffi > 0 and other.diffi > 0:
	    if self.diffi <= other.diffi:
		return mynum
	    elif self.diffi > other.diffi:
		return myother
	if self.diffi == 0:
	    return mynum
	if other.diffi == 0:
	    return myother
	return 0
	
class GraphResult:

    def __init__(self, mParameters):

	print "Submitting new Graph... " + mParameters.stringify()

	self.parameters = mParameters
	filename = self.parameters.generate()
	print filename

	self.BLYP = GraphVals(filename)
	self.HF = GraphVals(filename + "HF")
	self.B3LYP = GraphVals(filename + "B3LYP")
	self.BHHLYP = GraphVals(filename + "BHHLYP")

    def draw(self, name):
	plt.plot(X, self.BLYP.q, 'k', lw=8)
        plt.plot(X, self.HF.q, 'r', lw=8)
	plt.plot(X, self.B3LYP.q, 'b', lw=8)
	plt.plot(X, self.BHHLYP.q, 'g', lw=8)
	
        # plt.ylim([-1.5, 1])
        plt.ylabel('Relative energy (eV)', fontsize=48, fontweight='bold')
        plt.xlabel('Charge on equilibrium Kevan structure', fontsize=48, fontweight='bold')
        fig.set_size_inches(28, 22)
        plt.savefig(name+"-spline.png")
        plt.clf()

    def next_params(self, other):
	p1 = self.BLYP.newPara(other.BLYP, self.parameters.con, other.parameters.con)
	p2 = self.HF.newPara(other.HF, self.parameters.HFcon, other.parameters.HFcon)
	p3 = self.B3LYP.newPara(other.B3LYP, self.parameters.B3con, other.parameters.B3con)
	p4 = self.BHHLYP.newPara(other.BHHLYP, self.parameters.BHHcon, other.parameters.BHHcon)
	return Parameters(p1, p2, p3, p4)
 
    def pChallenge(self, a, b, diffi):
	if a > b:
	    if diffi > 0:
		return b
	    else:
		return a
	elif a < b:
	    if diffi < 0:
		return b
	    else:
		return a
	return a

    def challenge(self, other):
	print "A new challenger approaches!"
	print "Challenger self: " + self.stringify()
	print "Challenger other: (boo!) " + other.stringify()

	paramBox = self.next_params(other)
	newGraph = GraphResult(paramBox)
	print "The horrific amalgamation is " + newGraph.stringify()

	newcon = newGraph.pChallenge(self.parameters.con, other.parameters.con, newGraph.BLYP.diffi)
	newHFcon = newGraph.pChallenge(self.parameters.HFcon, other.parameters.HFcon, newGraph.HF.diffi)
	newB3con = newGraph.pChallenge(self.parameters.B3con, other.parameters.B3con, newGraph.B3LYP.diffi)
	newBHHcon = newGraph.pChallenge(self.parameters.BHHcon, other.parameters.BHHcon, newGraph.BHHLYP.diffi)

	return [ newGraph, Parameters(newcon, newHFcon, newB3con, newBHHcon) ]

    def isEqualTo(self, other):
        return self.parameters.isEqualTo(other.parameters)

    def diffify(self) :
        return "Diffis: BLYP %s, HF %s, B3LYP %s, BHHLYP %s" % (self.BLYP.diffi, self.HF.diffi, self.B3LYP.diffi, self.BHHLYP.diffi)

    def stringify(self) :
	return self.parameters.stringify() + " " + self.diffify()

    def conThing(self, a, b) :	#does not work in the current build!!!
        if abs(a - b) == 0.01:
	    return True
	if abs(b - a) == 0.01:
	    return True
	if abs(a - b) == 0:
	    return True
	return False

    def closer_to_0(self, a, b, apar, bpar):
        if abs(b) < abs(a):
	    return bpar
        return apar

    def checkStop(self, b):
	if self.conThing(self.parameters.con, b.parameters.con):
	    if self.conThing(self.parameters.HFcon, b.parameters.HFcon):
		if self.conThing(self.parameters.B3con, b.parameters.B3con):
		    if self.conThing(self.parameters.BHHcon, b.parameters.BHHcon):
			return True
	return False

class Parameters:
    
    def __init__(self, _con, _HFcon, _B3con, _BHHcon):
        self.con = round(_con, 2)
	self.HFcon = round(_HFcon, 2)
	self.B3con = round(_B3con, 2)
	self.BHHcon = round(_BHHcon, 2)

    def generate(self):
	return generate(self.con, self.HFcon, self.B3con, self.BHHcon, NAME)

    def isEqualTo(self, other):
	return (self.con == other.con) and (self.HFcon == other.HFcon) and (self.B3con == other.B3con) and (self.BHHcon == other.BHHcon)

    def stringify(self):
	return "Parameters: con %f, HFcon %f, B3con %f, BHHcon %f" % (self.con, self.HFcon, self.B3con, self.BHHcon)

def Execute():

    de80 = Parameters(80, 80, 80, 80)
    de0 = Parameters(1, 1, 1, 1)

    resultA = GraphResult(de80)
    print "de80: " + resultA.stringify()
    resultB = GraphResult(de0)
    print "de0: " + resultB.stringify()

    print "Draw!"
    resultA.draw("draw80")
    resultB.draw("draw0")
    
    looplist = []
    looplist.append(resultA)

    exceed = False
    loopCount = 0
    time.clock()

    while not resultA.isEqualTo(resultB) :
	print "Loop: %i" % loopCount
	loopCount += 1

	output = resultA.challenge(resultB)
	resultA = output[0]
	print "Result A: " + resultA.stringify()
	resultB = GraphResult(output[1])
	print "Result B: " + resultB.stringify()
	resultA.draw("drawopt")

	i = looplist[-1]
	
	if i.isEqualTo(resultA):
	    print "Repeated Result A broke the loop."
	    p1 = resultA.closer_to_0(resultA.BLYP.diffi, resultB.BLYP.diffi, resultA.parameters.con, resultB.parameters.con)
	    p2 = resultA.closer_to_0(resultA.HF.diffi, resultB.HF.diffi, resultA.parameters.HFcon, resultB.parameters.HFcon)
	    p3 = resultA.closer_to_0(resultA.B3LYP.diffi, resultB.B3LYP.diffi, resultA.parameters.B3con, resultB.parameters.B3con)
	    p4 = resultA.closer_to_0(resultA.BHHLYP.diffi, resultB.BHHLYP.diffi, resultA.parameters.BHHcon, resultB.parameters.BHHcon)
	    A = Parameters(p1, p2, p3, p4)
            resultA = GraphResult(A)
	    break

	looplist.append(resultA)
	
        #Does not work in the current build
	if resultA.checkStop(resultB):
	    p1 = resultA.closer_to_0(resultA.BLYP.diffi, resultB.BLYP.diffi, resultA.parameters.con, resultB.parameters.con)
	    p2 = resultA.closer_to_0(resultA.HF.diffi, resultB.HF.diffi, resultA.parameters.HFcon, resultB.parameters.HFcon)
	    p3 = resultA.closer_to_0(resultA.B3LYP.diffi, resultB.B3LYP.diffi, resultA.parameters.B3con, resultB.parameters.B3con)
	    p4 = resultA.closer_to_0(resultA.BHHLYP.diffi, resultB.BHHLYP.diffi, resultA.parameters.BHHcon, resultB.parameters.BHHcon)
	    A = Parameters(p1, p2, p3, p4)
            resultA = GraphResult(A)
	    break
	
	if loopCount >= 100 :
	    exceed = True
	    p1 = resultA.closer_to_0(resultA.BLYP.diffi, resultB.BLYP.diffi, resultA.parameters.con, resultB.parameters.con)
	    p2 = resultA.closer_to_0(resultA.HF.diffi, resultB.HF.diffi, resultA.parameters.HFcon, resultB.parameters.HFcon)
	    p3 = resultA.closer_to_0(resultA.B3LYP.diffi, resultB.B3LYP.diffi, resultA.parameters.B3con, resultB.parameters.B3con)
	    p4 = resultA.closer_to_0(resultA.BHHLYP.diffi, resultB.BHHLYP.diffi, resultA.parameters.BHHcon, resultB.parameters.BHHcon)
	    A = Parameters(p1, p2, p3, p4)
            resultA = GraphResult(A)
	    break
   
    if exceed:
	print "Hit 100 loops."
   
    print "Loop exited in %s seconds." % time.clock()

    resultA.draw("drawopt")

    print "Optimal graph drawn in %i loops." % loopCount
    print "Final " + resultA.stringify()

Execute()
#deopt = Parameters(7.755299, 1, 2.850889, 1.504499)
#optGraph = GraphResult(deopt)
#optGraph.draw("drawopt")
