import matplotlib.pyplot as plt
from os import mkdir, path
# This program plots a group of pair distribution function
if not path.exists('g-r relationship plot'):
    mkdir('g-r relationship plot')

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
    plt.figure(i)
    #plt.subplot(3,4,i+1)
    plt.plot(r, g, '.-')
    plt.plot(x, y, '--',color='r')
    plt.title("T"+str(round(nnn,1)) + " pair distribution function-distance relationship plot")
    plt.ylim([0, 7.5])
    plt.grid(0.1, linestyle='--')
    plt.xlabel('r')
    plt.ylabel('g')
    plt.grid(color = '0.8');
    plt.savefig("g-r relationship plot/T"+str(round(nnn,1))+" g-r relationship plot"+".png")
    #plt.show()
    r.clear()
    g.clear()


