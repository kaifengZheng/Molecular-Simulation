from matplotlib import spines
import matplotlib.pyplot as plt
import numpy as np
from os import path,mkdir

##This program is for drawing plots of diffirent properties during melting simulation.
#                         *Energy-temperature
#                         *pressure-temperature
#                         *heat capacity-temperature
#                         *mean square displacement-temperature

if not path.exists('properties plot'):
    mkdir('properties plot')

lines = []
properties = []
Cv = []
T = []
P = []
energy = []
displacement1 = []
displacement2 = []
displacement3 = []
displacement4 = []
displacement5 = []
displacement = []
number = 0.0
filenum = 12
for nm in range(0,filenum):
    number = number + 0.3
    name = "T"+str(round(number,1))+"/properties"
    with open(name,"r") as file1:
        for line in file1:
            l = ' '.join(line.split())
            lines.append(l)
    for i in range(0,len(lines)):
        properties.append(lines[i].split(' '))
    Cv.append(float(properties[0][2]))
    T.append(float(properties[0][5]))
    P.append(float(properties[1][2]))
    energy.append(float(properties[1][5]))
    displacement1.append(float(properties[2][8]))
    displacement2.append(float(properties[3][8]))
    displacement3.append(float(properties[4][8]))
    displacement4.append(float(properties[5][8]))
    displacement5.append(float(properties[6][8]))
    displacement.append([float(properties[2][8]),float(properties[3][8]),float(properties[4][8]),float(properties[5][8]),float(properties[6][8])])
    lines.clear()
    properties.clear()

#Energy-T
T_plot=plt.figure(1)
ax = T_plot.add_subplot(1,1,1)
ax.spines['bottom'].set_position(('data',0))
ax.spines['top'].set_color('none')
plt.plot(T,energy,'o-')
plt.title("Energy-T plot")
plt.xlabel('T')
plt.ylabel('Energy')
plt.grid(0.1,linestyle = '--')
plt.savefig("properties plot/Energy-T plot,png")


#plot Cv-T
#fitting by numpy.ployfit
T_array = np.array(T)
Cv_array = np.array(Cv)
Cv_mid = np.median(Cv_array)
print("The Cv is %.3f" %Cv_mid)
#plot
Cv_plot=plt.figure(2)
plt.plot(T,Cv,'o',label="data from calculation")
xs = [0,4]
ys = [Cv_mid,Cv_mid]
plt.plot(xs,ys,"--",color="red",label="fitting")
plt.title("Cv-T plot")
plt.xlabel('T')
plt.ylabel('Cv')
plt.ylim([0,5])
ytick=plt.yticks([0,1,2,Cv_mid,3,4,5],["0","1","2","2.696","3","4","5"])
plt.gca().get_yticklabels()[3].set_color('r')
plt.legend(loc="upper left")
plt.grid(0.1,linestyle = '--')
plt.savefig("properties plot/Cv-T plot")


#plot P-T
P_plot = plt.figure(3)
plt.plot(T,P,'o-')
plt.title("P-T plot")
plt.xlabel('T')
plt.ylabel('P')
plt.grid(0.1,linestyle = '--')
plt.savefig("properties plot/P-T plot.png")


#plot MSD VS steps(time)
Dis_plot = plt.figure(4)
d1=plt.plot(T,displacement1,'o-',label = "MSD at 195th step")
d2=plt.plot(T,displacement2,'o-',label = "MSD at 390th step")
d3=plt.plot(T,displacement3,'o-',label = "MSD at 585th step")
d4=plt.plot(T,displacement4,'o-',label = "MSD at 780th step")
d5=plt.plot(T,displacement5,'o-',label = "MSD at 975th step")
lengend = plt.legend(loc = "upper left")

plt.xlabel('T')
plt.ylabel('displacement')
plt.title('Displacement-T plot')
plt.grid(0.1,linestyle = '--')
plt.savefig('properties plot/Displacement-T plot.png')

#plot MSDs VS time and Temperatures
step = [1,2,3,4,5]
xticks = ["195th step","3905h step","585th step","780th step","975th step"]
TT = 0
for i in range(0,len(displacement)):
    TT = TT + 0.3
    if TT<=2.2:
        p1=plt.figure(5,figsize=(10,8))
        plt.plot(step,displacement[i][:],'o-',label="Displacement under T="+str(round(TT,1)))
        plt.ylim([0, 0.16])
        plt.legend(loc="upper left")
        plt.xticks(step, xticks, rotation=45)
        plt.grid(0.1, linestyle='--')
        plt.title("Displacements over different temperature")
        plt.ylabel("Displacement")
    else:
        p2 = plt.figure(6, figsize=(10, 8))
        plt.plot(step, displacement[i][:], 'o-', label="Displacement under T=" + str(round(TT, 1)))
        plt.legend(loc="upper left")
        plt.xticks(step, xticks, rotation=45)
        plt.grid(0.1, linestyle='--')
        plt.title("Displacements over different temperature")
        plt.ylabel("Displacement") 

p1.savefig('properties plot/Displacements over different temperature1')
p2.savefig('properties plot/Displacements over different temperature2')
