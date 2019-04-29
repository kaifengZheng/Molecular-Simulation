import matplotlib.pyplot as plt
from os import mkdir, path
#This program draws pairs of g-r plots, one pair is below melting point
#one is above melting point.
if not path.exists('g-r relationship plot4'):
    mkdir('g-r relationship plot4')

r = []
g = []
nnn = 0
filenum = 12

x = [0,5]
y = [1,1]
for i in range(0,filenum):
    #filename = input("Enter directory name: ")
    nnn = nnn+0.3
    name = "T"+str(round(nnn,1)) + "/gr"
    with open(name, "r") as file1:
        for lines in file1:
            del_space = ' '.join(lines.split())
            list_num = del_space.split(' ')
            r.append(float(list_num[0]))
            g.append(float(list_num[1]))

    if i == 0:
        plt.figure(1)
        plt.subplot(1, 2, 1)
        plt.plot(r, g, '.-')
        plt.plot(x, y, '--', color='r')
        plt.grid(0.1, linestyle='--')
        plt.title("T" + str(round(nnn, 1)) + " g-r relationship plot")
        plt.xlabel('r')
        plt.ylabel('g')
        T0=str(round(nnn, 1))
    if i == 1:
        plt.subplot(1, 2, 2)
        plt.plot(r, g, '.-')
        plt.plot(x, y, '--', color='r')
        plt.grid(0.1, linestyle='--')
        plt.title("T" + str(round(nnn, 1)) + " g-r relationship plot")
        plt.xlabel('r')
        plt.ylabel('g')
        plt.tight_layout()
        plt.savefig("g-r relationship plot4/T"+T0+"-"+str(round(nnn,1))+" g-r relationship plot"+".png")
    if i == 8:
        plt.figure(2)
        plt.subplot(1, 2, 1)
        plt.plot(r, g, '.-')
        plt.plot(x, y, '--', color='r')
        plt.grid(0.1, linestyle='--')
        plt.title("T" + str(round(nnn, 1)) + " g-r relationship plot")
        plt.xlabel('r')
        plt.ylabel('g')
        T0 = str(round(nnn,1))
    if i == 9:
        plt.subplot(1, 2, 2)
        plt.plot(r, g, '.-')
        plt.plot(x, y, '--', color='r')
        plt.grid(0.1, linestyle='--')
        plt.title("T" + str(round(nnn, 1)) + " g-r relationship plot")
        plt.xlabel('r')
        plt.ylabel('g')
        plt.tight_layout()
        plt.savefig("g-r relationship plot4/T"+T0+"-"+str(round(nnn,1))+ " g-r relationship plot" + ".png")
    #plt.show()
    r.clear()
    g.clear()


