""" Latest version_ edited on 13-02-2023"""
import pandas as pd
import os
import re
import sys
print('****************************************************************************************************************************************')
print("####################################################### BADER.PY ######################################################################")
print("****************************************************************************************************************************************")
print("The programme reads ACF.dat and writes the bader effective charge of each elements in bader.txt file. The POTCAR and POSCAR files are also required")
df = pd.read_csv('ACF.dat', delimiter=r"\s+" )
y_old = list(df.CHARGE)
bader_pop = [x for x in y_old if str(x) != 'nan']
#print(bader_pop)


elements = []
total = []
number = []
h = []
total_ions = []
atomic_number = []
x = []
extract_v = []

os.system("grep VRHFIN POTCAR >potcar.txt")
os.system("grep ZVAL POTCAR >potcar_new.txt")
f = open('potcar_new.txt')
for line in f:           # for finding the number of velence electrons from the POTCAR file
    new_lines = line.strip().split()
    extract_v.append(new_lines[-4:][0])
f.close()
number = [float(i) for i in extract_v]

f = open('potcar.txt')
for line in f:
	lines = line.strip().split()
	total.append(lines)
f.close()

for i in range(len(total)):
        p = total[i][1]
        x.append(re.findall(r"\w+", p))
for i in range(len(x)):
	elements.append(x[i][0])

result = ', '.join(f"{ele}: {elem}" for ele, elem in zip(elements, number))
print(f"The number of valence electrons from POTCAR for respective elements are {result}. Please check!!!")
os.system("rm potcar_new.txt")
poscar = open("POSCAR")

pos = []
for line in poscar:
	lines = line.strip().split()
	pos.append(lines)
poscar.close()
fifth = [int(s) for s in pos[5] if s.isdigit()]
sixth = [int(s) for s in pos[6] if s.isdigit()]
total_ions = pos[6]
if len(fifth)==0:
	total_ions = sixth
else:
	total_ions = fifth

valence_e = []
valence = []
for i in range(len(elements)):
	valence_e.append([number[i] for _ in range(total_ions[i])])
	valence= valence + valence_e[0]
	valence_e = []
n_elements = []
all_elements = []
for i in range(len(elements)):
	n_elements.append([elements[i] for _ in range(total_ions[i])])
	all_elements = all_elements + n_elements[0]
	n_elements = []
if len(valence) != len(bader_pop):
	print("No of ions is not correct")
	sys.exit('Error in giving the no of ions')
bader = []
for i in range(len(bader_pop)):
	bader.append(valence[i]-bader_pop[i])
p=0
#bader1=[]
for i in range(len(total_ions)):
	bader1=bader[p:p+total_ions[i]]
	av = sum(bader1)/ total_ions[i]
	print("The average of bader charge for "+elements[i]+" : " + str(av))
	p=p+total_ions[i]

g= open("bader.txt","w+")
g.write("element"+"\t"+"bader at.charge"+"\n")
g.write("-----------------------------"+"\n")
for i in range(len(bader)):
	g.write(str(all_elements[i])+"\t"+"\t"+str(bader[i])+"\n")
g.close()
