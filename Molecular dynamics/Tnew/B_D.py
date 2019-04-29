import matplotlib.pyplot as plt
import numpy as np
from os import mkdir,path

##This program is for drawing plots of Thermal motion and diffusion coefficient during melting simulation.
if not path.exists('properties plot'):
    mkdir('properties plot')
lines = []
properties = []
displacement = []
slope= []
T=[]
slope_all = []

#mean_square displacements for temperatures, diffusion coefficients and thermal motions save in a dictionary data type.
displacement_T = dict()
D = dict()
B = dict()

number = 0.0
#the step size differences of collections of mean_square displacements
difference = 195
# Temperature files
filenum = 12
# extract data from files
for nm in range(0,filenum):
    number = number + 0.3
    name = "T"+str(round(number,1))+"/properties"
    with open(name,"r") as file1:
        for line in file1:
            l = ' '.join(line.split())
            lines.append(l)
    for i in range(0,len(lines)):
        properties.append(lines[i].split(' '))
    T.append(float(properties[0][5]))
    displacement.append([float(properties[2][8]),float(properties[3][8]),float(properties[4][8]),float(properties[5][8]),float(properties[6][8])])
    displacement_T.update({float(properties[0][5]):displacement[nm]})
    lines.clear()
    properties.clear()
# Thermal motion can be calculated from the average of mean_square displacements below the melting point
for elements in displacement_T.keys():
    i = 0;
    if elements<=2.2:
        ave_dis = round(sum(displacement_T[elements])/len(displacement_T[elements]),6)
        B.update({elements:ave_dis})
    else:
    #diffusion coefficients can be calculated from the slope of mean_square displacement above the melting point.
        for i in range(0,len(displacement_T[elements])-1):
            slope.append(round(((displacement_T[elements][i+1]-displacement_T[elements][i])/(T[i+1]-T[i])),6))
            slope_ave = round(sum(slope)/len(slope),6)
            D.update({elements:round(slope_ave/6.0,6)})
            slope.clear()
#linear fitting for thermal motions
TB = np.fromiter(B.keys(),dtype=float)
BB = np.fromiter(B.values(),dtype=float)
z = np.polyfit(TB,BB,1)
p = np.poly1d(z)
xs = [0,2.1]
xs = np.round(xs,1)
ys = [p(0),p(2.1)]
ys = np.round(ys,5)

#linear fitting for diffuaion coeffients
TD = np.fromiter(D.keys(),dtype=float)
DD = np.fromiter(D.values(),dtype=float)
z = np.polyfit(TD,DD,1)
pp = np.poly1d(z)
xss = [2.2,3.7]
xss = np.round(xss,1)
yss = [pp(2.2),pp(3.7)]
yss = np.round(yss,5)

#Thermal motion plots
fig=plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
l1=plt.plot(TB,BB,'o',color='b',label = 'Thermal motion')
l2=plt.plot([2.2]*2,[0.001,0.3],"--",color='r',label = 'melting point')
l3=plt.plot(xs,ys,'-',color="cyan",label = "linear fitting")
plt.legend(loc='upper left')
plt.xlabel("T")
plt.grid(0.1,linestyle = '--')
plt.ylabel("Thermal Motion(B)")
plt.title("Thermal Motion(B) VS T Plot")
plt.ylim([0,0.08])
plt.xlim([0.0,2.3])
plt.xticks([0,0.22,0.44,0.66,0.88,1.10,1.32,1.54,1.76,1.98,2.20,2.42],[0,0.22,0.44,0.66,0.88,1.10,1.32,1.54,1.76,1.98,2.20,2.42])
plt.text(0.1,0.03,'B='+str(round(p[1],3))+'T'+str(round(p[0],3)))
#diffusion coefficients plots
plt.subplot(1,2,2)
l4=plt.plot(TD,DD,'o',color='b',label = 'Diffusion Coefficient')
l5=plt.plot([2.2]*2,[0.001,0.3],"--",color='r',label = 'melting point')
l6=plt.plot(xss,yss,'-',color="cyan",label = "linear fitting")
plt.title("Diffusion Coefficient(D) VS T Plot")
plt.legend(loc = 'upper left')
plt.xlabel("T")
plt.ylabel('Diffusion Coefficient(D)')
plt.text(2.8,0.1,'D='+str(round(pp[1],3))+'T'+str(round(pp[0],3)))
plt.ylim([0,0.3])
plt.grid(0.1,linestyle = '--')
#keep plots tight but not cross each other
plt.tight_layout() 
plt.savefig('properties plot/Thermal Motion(B) and Diffusion Coefficient(D) VS Temperature Plot')
#plt.show()



