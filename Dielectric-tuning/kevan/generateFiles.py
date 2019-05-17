import numpy as np
import os

path = os.path.abspath('.')

func = ["BLYP", "HF", "B3LYP", "BHHLYP"]
gap = [0, 1, 2] # a
charge = ['-1', '0'] # b
multi = ['2', '1']
name = ['a', '']


def clear(filename):
    nm = filename
    method = ["", "HF", "B3LYP", "BHHLYP"]
    method[0] = ""
    for m in method:
	for a in gap:
	    for b in name:
		if os.path.exists(path + "/" + nm + m + str(b) + str(a) + ".in"):
		    os.system("rm " + nm + m + str(b) + str(a) + ".in")
		if os.path.exists(path + "/" + nm + m + str(b) + str(a) + ".in"):
		    os.system("rm " + nm + m + str(b) + str(a) + ".in")
		if os.path.exists(path + "/" + nm + m + str(b) + ".out"):
		    os.system("rm " + nm + m + str(b) + ".out")
		if os.path.exists(path + "/" + nm + m + str(b) + ".out"):
		    os.system("rm " + nm + m + str(b) + ".out")

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
        a = 0
        while a < len(gap):
	    Hdist = 1.913795 + gap[a]
	    Odist = Hdist + 0.97659
            b = 0
            while b < len(name):
                #input_file = open('%s%s%s.in' % (name[b], str(int(gap[a]*10))), 'w')
                #if not os.path.exists(path + '/water%s%s.in' % (func[m], name[b])):
                if m == 0:
                    input_file = open('%s%s%s.in' % (nm, name[b], gap[a]), 'w')
                    input_file.write('$rem                                                     \n' )
                    input_file.write('    BASIS aug-cc-pVDZ                                    \n' )
                    input_file.write('    METHOD %s                                            \n' %  func[m])
                    input_file.write('    SOLVENT_METHOD PCM                                   \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$pcm                                                     \n' )
                    input_file.write('        Theory CPCM                                      \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$chem_sol                                                \n' )
                    input_file.write('    ReadRadii                                            \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$van_der_waals                                           \n' )
                    input_file.write('    1                                                    \n' )
                    input_file.write('    0 3.                                                 \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$solvent                                                 \n' )
                    input_file.write('        Dielectric %.6f                                  \n' %  de[m])
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$molecule                                                \n' )
                    input_file.write('%s %s                                                    \n' % (charge[b], multi[b]))
                    input_file.write('@H1                                                      \n' )
                    input_file.write('H2    1    %.6f                                          \n' %  Hdist)
                    input_file.write('H3    1    %.6f    2    90.000                           \n' %  Hdist)
                    input_file.write('H4    1    %.6f    2    90.000    3    180.000           \n' %  Hdist)
                    input_file.write('H5    1    %.6f    2    90.000    3    90.000            \n' %  Hdist)
                    input_file.write('H6    1    %.6f    2    90.000    3    -90.000           \n' %  Hdist)
                    input_file.write('H7    1    %.6f    3    90.000    2    180.000           \n' %  Hdist)
                    input_file.write('O8    1    %.6f    2    90.000    3    180.000           \n' %  Odist)
                    input_file.write('O9    1    %.6f    2    90.000    3    90.000            \n' %  Odist)
                    input_file.write('O10    1    %.6f    2    90.000    3    -90.000          \n' %  Odist)
                    input_file.write('O11    1    %.6f    2    90.000    3    0.000            \n' %  Odist)
                    input_file.write('O12    1    %.6f    3    90.000    2    180.000          \n' %  Odist)
                    input_file.write('O13    1    %.6f    3    90.000    2    0.000            \n' %  Odist)
                    input_file.write('H14    8    0.962825    1    102.642    2    35.866      \n' )
                    input_file.write('H15    9    0.962825    1    102.642    2    35.866      \n' )
                    input_file.write('H16    10    0.962825    1    102.642    2    144.134    \n' )
                    input_file.write('H17    11    0.962825    1    102.642    2    144.134    \n' )
                    input_file.write('H18    12    0.962825    1    102.642    3    144.134    \n' )
                    input_file.write('H19    13    0.962825    1    102.642    3    35.866     \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    b += 1
		else:
                    input_file = open('%s%s%s%s.in' % (nm, func[m], name[b], gap[a]), 'w')
                    input_file.write('$rem                                                     \n' )
                    input_file.write('    BASIS aug-cc-pVDZ                                    \n' )
                    input_file.write('    METHOD %s                                            \n' %  func[m])
                    input_file.write('    SOLVENT_METHOD PCM                                   \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$pcm                                                     \n' )
                    input_file.write('        Theory CPCM                                      \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$chem_sol                                                \n' )
                    input_file.write('    ReadRadii                                            \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$van_der_waals                                           \n' )
                    input_file.write('    1                                                    \n' )
                    input_file.write('    0 3.                                                 \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$solvent                                                 \n' )
                    input_file.write('        Dielectric %.6f                                  \n' %  de[m])
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('$molecule                                                \n' )
                    input_file.write('%s %s                                                    \n' % (charge[b], multi[b]))
                    input_file.write('@H1                                                      \n' )
                    input_file.write('H2    1    %.6f                                          \n' %  Hdist)
                    input_file.write('H3    1    %.6f    2    90.000                           \n' %  Hdist)
                    input_file.write('H4    1    %.6f    2    90.000    3    180.000           \n' %  Hdist)
                    input_file.write('H5    1    %.6f    2    90.000    3    90.000            \n' %  Hdist)
                    input_file.write('H6    1    %.6f    2    90.000    3    -90.000           \n' %  Hdist)
                    input_file.write('H7    1    %.6f    3    90.000    2    180.000           \n' %  Hdist)
                    input_file.write('O8    1    %.6f    2    90.000    3    180.000           \n' %  Odist)
                    input_file.write('O9    1    %.6f    2    90.000    3    90.000            \n' %  Odist)
                    input_file.write('O10    1    %.6f    2    90.000    3    -90.000          \n' %  Odist)
                    input_file.write('O11    1    %.6f    2    90.000    3    0.000            \n' %  Odist)
                    input_file.write('O12    1    %.6f    3    90.000    2    180.000          \n' %  Odist)
                    input_file.write('O13    1    %.6f    3    90.000    2    0.000            \n' %  Odist)
                    input_file.write('H14    8    0.962825    1    102.642    2    35.866      \n' )
                    input_file.write('H15    9    0.962825    1    102.642    2    35.866      \n' )
                    input_file.write('H16    10    0.962825    1    102.642    2    144.134    \n' )
                    input_file.write('H17    11    0.962825    1    102.642    2    144.134    \n' )
                    input_file.write('H18    12    0.962825    1    102.642    3    144.134    \n' )
                    input_file.write('H19    13    0.962825    1    102.642    3    35.866     \n' )
                    input_file.write('$end                                                     \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    input_file.write('                                                         \n' )
                    b += 1
            a += 1
	m += 1
           
