import numpy as np
import os

path = os.path.abspath('.')

func = ["BLYP", "HF", "B3LYP", "BHHLYP"]
#gap = [0., 1., 2.] # a
charge = ['-1', '0'] # b
multi = ['2', '1']
name = ['a', '']

def clear_ins():
    if os.path.exists(path + 'water.in'):
	os.system("rm water.in")
    if os.path.exists(path + '/watera.in'):
	os.system("rm watera.in")
    if os.path.exists(path + '/waterHF.in'):
	os.system("rm waterHF.in")
    if os.path.exists(path + '/waterHFa.in'):
	os.system("rm waterHFa.in")
    if os.path.exists(path + '/waterB3LYP.in'):
	os.system("rm waterB3LYP.in")
    if os.path.exists(path + '/waterB3LYPa.in'):
	os.system("rm waterB3LYPa.in")
    if os.path.exists(path + '/waterBHHLYP.in'):
	os.system("rm waterBHHLYP.in")
    if os.path.exists(path + '/waterBHHLYPa.in'):
	os.system("rm waterBHHLYPa.in")

def clear_outs():
    if os.path.exists(path + '/water.out'):
	os.system("rm water.out")
    if os.path.exists(path + '/watera.out'):
	os.system("rm watera.out")
    if os.path.exists(path + '/waterHF.out'):
	os.system("rm waterHF.out")
    if os.path.exists(path + '/waterHFa.out'):
	os.system("rm waterHFa.out")
    if os.path.exists(path + '/waterB3LYP.out'):
	os.system("rm waterB3LYP.out")
    if os.path.exists(path + '/waterB3LYPa.out'):
	os.system("rm waterB3LYPa.out")
    if os.path.exists(path + '/waterBHHLYP.out'):
	os.system("rm waterBHHLYP.out")
    if os.path.exists(path + '/waterBHHLYPa.out'):
	os.system("rm waterBHHLYPa.out")

def generate_ins(con, HFcon, B3con, BHHcon):
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
                    input_file = open('water%s.in' % name[b], 'w')
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
                    input_file = open('water%s%s.in' % (func[m], name[b]), 'w')
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

