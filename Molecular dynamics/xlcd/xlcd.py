import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols,solve,Eq
from os import path,mkdir
# This program is used to calculate thermal expansion of Argon
if not path.exists('properties plot'):
    mkdir('properties plot')

lines = []
properties = []
T_P = []
a = 0
lattice = dict()
number = 0.0
Tfile = 4                                         #number of Temperature files will be used
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

#solver for optimal T points using linear fitting over P.T
x = symbols('x')
T_optimal = dict()
for elements in lattice.keys():
    T = np.array(lattice.get(elements)[0])
    P = np.array(lattice.get(elements)[1])
    z = np.polyfit(T,P,1)
    p = np.poly1d(z)
    T_optimal.update({elements:solve(Eq(p(x),0),x)})
T_optimal

#convert dictionary keys and values to numpy array
keys = np.fromiter(T_optimal.keys(),dtype = float)
values = list(T_optimal.values())
values = np.array(values,float).reshape(-1)
#force the first point (0,1.557)
new_values = values-values[0]
#plot
plt.plot(new_values,keys,'o',label="Data from calculation")
zz = np.polyfit(new_values,keys,1)
pp = np.poly1d(zz)
xs = [0.1 * i for i in range(10)]
xs = np.round(xs,1)
ys = [pp(x) for x in xs]
ys = np.round(ys,5)
#Thermal Expansion Coefficient
Therm_exp = (ys[4]-pp[0])/((xs[4]-0)*pp[0])
print("Thermal expansion coefficient = %.3f" %Therm_exp)
plt.plot(xs,ys,'-',color="red",label = "linear fitting")
plt.legend()
plt.xlabel("Optimal Temperature(T)")
plt.ylabel("Lattice Constant(a)") 
plt.grid(0.1, linestyle='--')
plt.title("Lattice Constant(a) VS Temperature Plot")
plt.text(0.4,1.58,'a='+str(round(pp[1],3))+'T+'+str(round(pp[0],3)))
plt.savefig('properties plot/Lattice Constant-optimal Temperature plot.png')
plt.show()
