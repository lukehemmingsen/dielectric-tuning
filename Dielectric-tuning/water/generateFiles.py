import numpy as np
import os

path = os.path.abspath('.')

func = ["BLYP", "HF", "B3LYP", "BHHLYP"]
#gap = [0., 1., 2.] # a
charge = ['-1', '0'] # b
multi = ['2', '1']
name = ['a', '']


def clear_ins(filename):
    nm = filename
    if os.path.exists(path + "/" + nm + ".in"):
	os.system("rm " + nm + ".in")
    if os.path.exists(path + "/" + nm + "a.in"):
	os.system("rm " + nm + "a.in")
    if os.path.exists(path + "/" + nm + "HF.in"):
	os.system("rm " + nm + "HF.in")
    if os.path.exists(path + "/" + nm + "HFa.in"):
	os.system("rm " + nm + "HFa.in")
    if os.path.exists(path + "/" + nm + "B3LYP.in"):
	os.system("rm " + nm + "B3LYP.in")
    if os.path.exists(path + "/" + nm + "B3LYPa.in"):
	os.system("rm " + nm + "B3LYPa.in")
    if os.path.exists(path + "/" + nm + "BHHLYP.in"):
	os.system("rm waterBHHLYP.in")
    if os.path.exists(path + "/" + nm + "BHHLYPa.in"):
	os.system("rm " + nm + "BHHLYPa.in")

def clear_outs(filename):
    nm = filename
    if os.path.exists(path + "/" + nm + ".out"):
	os.system("rm " + nm + ".out")
    if os.path.exists(path + "/" + nm + "a.out"):
	os.system("rm " + nm + "a.out")
    if os.path.exists(path + "/" + nm + "HF.out"):
	os.system("rm " + nm + "HF.out")
    if os.path.exists(path + "/" + nm + "HFa.out"):
	os.system("rm " + nm + "HFa.out")
    if os.path.exists(path + "/" + nm + "B3LYP.out"):
	os.system("rm " + nm + "B3LYP.out")
    if os.path.exists(path + "/" + nm + "B3LYPa.out"):
	os.system("rm " + nm + "B3LYPa.out")
    if os.path.exists(path + "/" + nm + "BHHLYP.out"):
	os.system("rm waterBHHLYP.out")
    if os.path.exists(path + "/" + nm + "BHHLYPa.out"):
	os.system("rm " + nm + "BHHLYPa.out")

def generate_ins(con, HFcon, B3con, BHHcon, filename):
    nm = filename
    dielectric = round(con, 4)
    HFdielectric = round(HFcon, 4)
    B3dielectric = round(B3con, 4)
    BHHdielectric = round(BHHcon, 4)
    de = [dielectric, HFdielectric, B3dielectric, BHHdielectric]
    m = 0
    while m < len(func):
        #if not os.path.exists(path + '/%s' % func[m]):
        #    os.makedirs(path + '/%s' % func[m])
        #os.chdir(path + '/%s' % func[m])
        #a = 0
        #while a < len(gap):
        b = 0
        while b < len(name):
            #input_file = open('%s%s.in' % (name[b], str(int(gap[a]*10))), 'w')
            #if not os.path.exists(path + '/water%s%s.in' % (func[m], name[b])):
                if m == 0:
                    input_file = open('%s%s.in' % (nm, name[b]), 'w')
                    input_file.write('$rem                                                     \n' )
                    input_file.write('    BASIS 6-31G                                            \n' )
                    input_file.write('    METHOD %s                                              \n' %  func[m])
                    input_file.write('    SOLVENT_METHOD PCM                                     \n' )
                    input_file.write('    JOBTYPE OPT                                            \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$pcm                                                     \n' )
                    input_file.write('        Theory CPCM                                      \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$solvent                                                 \n' )
                    input_file.write('        Dielectric %.6f                                  \n' %  de[m])
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$molecule                                                \n' )
                    input_file.write('%s %s                                                    \n' % (charge[b], multi[b]))
                    input_file.write('H        -0.759 0. 0.                                    \n' )
                    input_file.write('O        0. 0.588 0.                                     \n' )
                    input_file.write('H        0.759 0. 0.                                     \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    b += 1
                    #a += 1
                else:
                    input_file = open('%s%s%s.in' % (nm, func[m], name[b]), 'w')
                    input_file.write('$rem                                                     \n' )
                    input_file.write('    BASIS 6-31G                                            \n' )
                    input_file.write('    METHOD %s                                              \n' %  func[m])
                    input_file.write('    SOLVENT_METHOD PCM                                     \n' )
                    input_file.write('    JOBTYPE OPT                                            \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$pcm                                                     \n' )
                    input_file.write('        Theory CPCM                                      \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$solvent                                                 \n' )
                    input_file.write('        Dielectric %.6f                                  \n' %  de[m])
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$molecule                                                \n' )
                    input_file.write('%s %s                                                    \n' % (charge[b], multi[b]))
                    input_file.write('H        -0.759 0. 0.                                    \n' )
                    input_file.write('O        0. 0.588 0.                                     \n' )
                    input_file.write('H        0.759 0. 0.                                     \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    b += 1
                    #a += 1
	m += 1
           
def generate_sub():
    if os.path.exists(path + '/water.sub'):
        os.system("rm water.sub")
    sub_file = open('water.sub', 'w')
    sub_file.write('#!/bin/bash                                              \n ' )
    sub_file.write('#PBS -P fr18                                             \n ' )
    sub_file.write('#PBS -q express                                           \n ' )
    sub_file.write('#PBS -l walltime=00:05:00,mem=2GB                         \n ' )
    sub_file.write('#PBS -l wd                                               \n ' )
    sub_file.write('#PBS -l ncpus=4                                          \n ' )
    sub_file.write('                                                         \n ' )
    sub_file.write('module load qchem                                        \n ' )
    sub_file.write('                                                         \n ' )
    sub_file.write('qchem -nt 4 water.in > water.out                         \n ' )
    sub_file.write('qchem -nt 4 watera.in > watera.out                       \n ' )
    sub_file.write('qchem -nt 4 waterHF.in > waterHF.out                     \n ' )
    sub_file.write('qchem -nt 4 waterHFa.in > waterHFa.out                   \n ' )
    sub_file.write('qchem -nt 4 waterB3LYP.in > waterB3LYP.out               \n ' )
    sub_file.write('qchem -nt 4 waterB3LYPa.in > waterB3LYPa.out             \n ' )
    sub_file.write('qchem -nt 4 waterBHHLYP.in > waterBHHLYP.out             \n ' )
    sub_file.write('qchem -nt 4 waterBHHLYPa.in > waterBHHLYPa.out           \n ' )
    sub_file.write('                                                         \n ' )

