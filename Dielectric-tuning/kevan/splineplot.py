import numpy as np

def spline(x, a_ene, a_homo, n_ene, n_lumo):
    dE = a_ene - n_ene
    q = x * (dE) + x * (1-x) * ((n_lumo - (dE)) * (1-x) + (-a_homo + (dE)) * x)
#     q = q - q[0]
    q = 27.2114*q #unit conversion Hartrees to eV
    return q

def diffi(x, a_ene, a_homo, n_ene, n_lumo):
    dE = a_ene - n_ene
    q = x * (1-x) * ((n_lumo - dE) * (1-x) + (-a_homo + dE) * x)
    q = 27.2114*q
    return q

def transfer(x, a_ene, a_homo, n_ene, n_lumo):
    x2 = -(x - 1)
    q = (spline(x, a_ene, a_homo, n_ene, n_lumo) + spline(x2, a_ene, a_homo, n_ene, n_lumo)) 
    return q

def charge_transfer(x, a_ene, a_homo, n_ene, n_lumo):
    q = transfer(x, a_ene, a_homo, n_ene, n_lumo) - transfer(0, a_ene, a_homo, n_ene, n_lumo)
    return q

def transfer_diffi(x, a_ene, a_homo, n_ene, n_lumo):
    x2 = -(x - 1)
    q = diffi(x, a_ene, a_homo, n_ene, n_lumo) + diffi(x2, a_ene, a_homo, n_ene, n_lumo) 
    return q

X = np.arange(0.,1.0,0.01) #defines a list of 100 points

def InputFileName(message):
    print message
    badChars = "<>:\"/\|?*"
    while True:
	x = raw_input()
	nameIsBad = False
	for cha in x:
	    if cha in badChars:
		nameIsBad = True
		break
	if not nameIsBad:
	    return x

def can_float(mstring) :
    if mstring.strip() == "" :
        return False
    try :
        float(mstring)
	return True
    except :
	return False

def get_last_number(mList):
    for s in mList[::-1]:
        if can_float(s) :
            return float(s)

def get_first_number(mList):
    for s in mList[::1]:
	if can_float(s):
	    return float(s)

def get_anion(filename):
    file = filename+"a.out"
    output = open(file,"r").read()
    if "Final energy is   " in output:
        last = output.split("Final energy is   ")[-1]
    elif "Total energy in the final basis set = " in output:
	last = output.split("Total energy in the final basis set = ")[-1]
    else:
	print "ERROR"
    ene_hold = last.split("\n")[0].strip()
    a_ene = float(ene_hold)
    orbitals1 = last.split("-- Occupied --")[-2].split("-- Virtual --")[0]
    orbitals2 = last.split("-- Occupied --")[-1].split("-- Virtual --")[0]
    orbitals_s1 = orbitals1.split("\n")
    orbitals_s2 = orbitals2.split("\n")
    for line in orbitals_s1:
	letters = "abcdefghijklmnopqrstvuwxyz"
	for x in letters:
	    if x in line.lower():
		orbitals_s1.remove(line) 
                break
    for line in orbitals_s1:
        if line.strip() == "":
            orbitals_s1.remove(line)
    for line in orbitals_s2:
	letters = "abcdefghijklmnopqrstvuwxyz"
	for x in letters:
	    if x in line.lower():
		orbitals_s2.remove(line)
		break
    for line in orbitals_s2:
        if line.strip() == "":
	    orbitals_s2.remove(line)
    a_homo1 = get_last_number(orbitals_s1[-1].strip().split(" "))
    a_homo2 = get_last_number(orbitals_s2[-1].strip().split(" "))
   # a_homo1 = float(orbitals_s1[-1].strip().split(" ")[-1].strip())
   # a_homo2 = float(orbitals_s2[-1].strip().split(" ")[-1].strip())
    a_homo = a_homo1 if a_homo1 > a_homo2 else a_homo2
    print (a_ene, a_homo)
    return (a_ene, a_homo)

#print get_anion("water")

def get_neutral(filename):
    file = filename+".out"
    output = open(file,"r").read()
    if "Final energy is   " in output:
        last = output.split("Final energy is   ")[-1]
    elif "Total energy in the final basis set = " in output:
	last = output.split("Total energy in the final basis set = ")[-1]
    n_ene = float(last.split("\n")[0].strip())
    orbitals1 = last.split("-- Virtual --")[-2].split("\n")[1]
    orbitals2 = last.split("-- Virtual --")[-1].split("\n")[1]
    n_lumo1 = get_first_number(orbitals1.strip().split(" "))
    n_lumo2 = get_first_number(orbitals2.strip().split(" "))
    if not n_lumo1 is float:
	n_lumo = n_lumo2
    print (n_ene, n_lumo)
    return (n_ene, n_lumo)

#print get_neutral("water")

