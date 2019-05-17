import numpy as np
import os

path = os.path.abspath('.')

func = ["BLYP", "HF", "B3LYP", "BHHLYP"]
charge = ["1", "0"] # b
multi = ["2", "1"]
name = ['c', '']


def clear(filename):
    nm = filename
    if not os.path.exists(path + "/ins/"):
	os.makedirs(path + "/ins")
    if not os.path.exists(path + "/outs/"):
	os.makedirs(path + "/outs")
    if os.path.exists(path + "/subs/" + nm + ".txt"):
	os.system("rm subs/" + nm + ".txt")
    method = ["", "HF", "B3LYP", "BHHLYP"]
    method[0] = ""
    for m in method:
	for b in name:
	    if os.path.exists(path + "/ins/" + nm + m + str(b) + ".in"):
		os.system("rm ins/" + nm + m + str(b) + ".in")
	    if os.path.exists(path + "/ins/" + nm + m + str(b) + ".in"):
		os.system("rm ins/" + nm + m + str(b) + ".in")
	    if os.path.exists(path + "/outs/" + nm + m + str(b) + ".out"):
		os.system("rm outs/" + nm + m + str(b) + ".out")
	    if os.path.exists(path + "/outs/" + nm + m + str(b) + ".out"):
		os.system("rm outs/" + nm + m + str(b) + ".out")

def readxyz():
    nameDict = {}
    for xyz in os.listdir(path):
	if ".xyz" in xyz:
	    lines = open(xyz, 'r').read()
	    xyz = str(xyz[:-4])
	    nameDict.update({xyz : lines})
    #print nameDict
    return nameDict
	    
def generate_ins(con, HFcon, B3con, BHHcon, filename):
    nm = filename
    os.system("echo '' > subs/" + nm + ".txt")
    dielectric = round(con, 4)
    HFdielectric = round(HFcon, 4)
    B3dielectric = round(B3con, 4)
    BHHdielectric = round(BHHcon, 4)
    de = [dielectric, HFdielectric, B3dielectric, BHHdielectric]
    nameDict = readxyz()
    if nm in nameDict and "0 1\n" in nameDict[nm]:
	lines = nameDict[nm].split("\n")
        m = 0
        while m < len(func):
            if not os.path.exists(path + "/ins"):
                os.makedirs(path + "/ins")
            b = 0
            while b < len(name):
                #input_file = open('%s%s%s.in' % (name[b], str(int(gap[a]*10))), 'w')
                #if not os.path.exists(path + '/water%s%s.in' % (func[m], name[b])):
                if m == 0:
		    print b
		    print (charge[b], multi[b])
                    input_file = open(path + '/ins/%s%s.in' % (filename, name[b]), 'w')
                    input_file.write('$rem                                                     \n' )
                    input_file.write('    BASIS 6-31G*                                         \n' )
                    input_file.write('    METHOD %s                                            \n' % func[m])
                    input_file.write('    SOLVENT_METHOD PCM                                   \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$pcm                                                     \n' )
                    input_file.write('        Theory CPCM                                      \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$solvent                                                 \n' )
                    input_file.write('        Dielectric %.6f                                  \n' % de[m])
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$molecule                                                \n' )
		    input_file.write('%s %s\n' % (charge[b], multi[b]))
                    for line in lines[2:]:
		        input_file.write(line + '      \n') 
		    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    b += 1
		else:
                    input_file = open(path + '/ins/%s%s%s.in' % (filename, func[m], name[b]), 'w')
                    input_file.write('$rem                                                     \n' )
                    input_file.write('    BASIS 6-31G*                                         \n' )
                    input_file.write('    METHOD %s                                            \n' % func[m])
                    input_file.write('    SOLVENT_METHOD PCM                                   \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$pcm                                                     \n' )
                    input_file.write('        Theory CPCM                                      \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$solvent                                                 \n' )
                    input_file.write('        Dielectric %.6f                                  \n' % de[m])
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$molecule                                                \n' )
		    input_file.write('%s %s\n' % (charge[b], multi[b])) 
                    for line in lines[2:]:
			input_file.write(line + '      \n')
	 	    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    b += 1
	    m += 1

def generate_sub(filename):
    if os.path.exists(path + "/subs/" + filename + ".sub"):
	os.system("rm " + path + "/subs/" + filename + ".sub")
    elif not os.path.exists(path + "/subs/"):
	os.makedirs(path + "/subs")
    os.system("cp splineplot.py subs/splineplot.py")
    os.system("cp generateFiles.py subs/generateFiles.py")
    sub_file = open(path + "/subs/" + filename + ".sub", 'w')
    sub_file.write('#!/bin/bash                                       \n ' )
    sub_file.write('#PBS -P fr18                                      \n ' )
    sub_file.write('#PBS -q normal                                    \n ' )
    sub_file.write('#PBS -l walltime=24:00:00,mem=2GB                 \n ' )
    sub_file.write('#PBS -l wd                                        \n ' )
    sub_file.write('#PBS -l ncpus=1                                   \n ' )
    sub_file.write('                                                  \n ' )
    sub_file.write('module load qchem                                 \n ' )
    sub_file.write('module load python/2.7.3                          \n ' )
    sub_file.write('module load python/2.7.3-matplotlib               \n ' )
    sub_file.write('                                                  \n ' )
    sub_file.write('cp init-plot.py subs/%s-plot.py                   \n ' % filename )
    sub_file.write('python subs/%s-plot.py                            \n ' % filename )
    sub_file.write('                                                  \n ' )
   
