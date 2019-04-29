import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols,solve,Eq
from os import path,mkdir
#This program is to show when lattice constant goes up, the melting point will falles down.
#I drawed P-T plots shows that situations.

if not path.exists('properties plot'):
    mkdir('properties plot')

lines = []
properties = []
T_P = []
a = 0
lattice = dict()
number = 0.0
Tfile =  6                                          #number of Temperature files will be used
xlcdfile = 4                                         #number of xlcd files will be contained in the calculation
for nnm in range(0,xlcdfile):
    a = round(1.557*(1.00+0.01*nnm),3)
    a_str = "%.3f" %a
    for nm in range(0, Tfile):
        number = number + 0.3
        name = "xlcd"+a_str+"/T"+str(round(number,1))+"/properties"
        with open(name,"r") as file1:
            for line in file1:
                l = ' '.join(line.split())
                lines.append(l)
        for i in range(0, len(lines)):
            properties.append(lines[i].split(' '))
        if lattice.__contains__(a) is False:
            lattice.update({a: [[float(properties[0][5])], [float(properties[1][2])]]})
        else:
            lattice.get(a)[0].append(float(properties[0][5]))
            lattice.get(a)[1].append(float(properties[1][2]))
        lines.clear()
        properties.clear()
    number = 0.0

i = 1
for elements in lattice.keys():
    if i<=2:
        p1=plt.figure(1,figsize=(10,5))
        plt.subplot(1, 2, i)
        plt.plot(lattice.get(elements)[0], lattice.get(elements)[1], 'o-', label="xlcd = " + str(elements))
        plt.legend(loc="upper left")
        plt.xticks([0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
        plt.xlabel("T")
        plt.ylabel("P")
        plt.grid(0.1, linestyle='--')
        plt.tight_layout()
        plt.title("xlcd = " + str(elements) + " P-T plots")
    if i>2:
        p2=plt.figure(2,figsize=(10,5))
        plt.subplot(1, 2, i-2)
        plt.plot(lattice.get(elements)[0], lattice.get(elements)[1], 'o-', label="xlcd = " + str(elements))
        plt.legend(loc="upper left")
        plt.xticks([0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
        plt.xlabel("T")
        plt.ylabel("P")
        plt.grid(0.1, linestyle='--')
        plt.tight_layout()
        plt.title("xlcd = " + str(elements) + " P-T plots")

    i = i+1
p1.savefig('properties plot/P-T plots over different lattice constants1')
p2.savefig('properties plot/P-T plots over different lattice constants2')
#plt.show()
