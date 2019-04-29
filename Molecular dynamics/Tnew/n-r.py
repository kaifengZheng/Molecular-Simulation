import matplotlib.pyplot as plt
from os import mkdir,path
# This program plots two figures for coordination numbers before melting
# and two figures for coordination numbers after melting
#                        *n(r)-r
if not path.exists('n-r relationship plot4'):
    mkdir('n-r relationship plot4')

r = []
n = []
T = 0
filenum = 12

for i in range(0,filenum):
    #filename = input("Enter directory name: ")
    T = T+0.3
    name = "T"+str(round(T,1)) + "/nr"
    with open(name, "r") as file1:
        for lines in file1:
            del_space = ' '.join(lines.split())
            list_num = del_space.split(' ')
            r.append(float(list_num[0]))
            n.append(float(list_num[1]))
    if i==0:
        plt.figure(1)
        plt.subplot(1, 2, 1)
        plt.plot(r, n, '.-', color='b')
        plt.grid(0.1, linestyle='--')
        plt.title("T" + str(round(T, 1)) + " n-r relationship plot")
        plt.xlabel('r')
        plt.ylabel('n')
        plt.ylim([0, r[-1]])
        plt.yticks(range(0, 50, 10), range(0, 50, 10))
        plt.xlim([0, 2])
        T0 = str(round(T,1))
    if i==1:
        plt.subplot(1, 2, 2)
        plt.plot(r, n, '.-', color='b')
        plt.grid(0.1, linestyle='--')
        plt.title("T" + str(round(T, 1)) + " n-r relationship plot")
        plt.xlabel('r')
        plt.ylabel('n')
        plt.ylim([0, r[-1]])
        plt.yticks(range(0, 50, 10), range(0, 50, 10))
        plt.xlim([0, 2])
        plt.tight_layout()
        plt.savefig("n-r relationship plot4/T" + T0+"-T"+str(round(T, 1)) + " n-r relationship plot" + ".png")
        plt.close(plt.figure(1))
    if i == 8:
        plt.figure(2)
        plt.subplot(1,2,1)
        plt.plot(r, n, '.-',color='b')
        plt.grid(0.1, linestyle='--')
        plt.title("T" + str(round(T, 1)) + " n-r relationship plot")
        plt.xlabel('r')
        plt.ylabel('n')
        plt.ylim([0, r[-1]])
        plt.yticks(range(0, 50, 10), range(0, 50, 10))
        plt.xlim([0, 2.2])
        T0 = str(round(T,1))
    if i == 9:
        plt.subplot(1, 2, 2)
        plt.plot(r, n, '.-', color='b')
        plt.grid(0.1, linestyle='--')
        plt.title("T" + str(round(T, 1)) + " n-r relationship plot")
        plt.xlabel('r')
        plt.ylabel('n')
        plt.ylim([0, r[-1]])
        plt.yticks(range(0, 50, 10), range(0, 50, 10))
        plt.xlim([0, 2.2])
        plt.tight_layout()
        plt.savefig("n-r relationship plot4/T"+ T0+"-T"+str(round(T, 1)) + " n-r relationship plot" + ".png")
        plt.close(plt.figure(1))
    #plt.show()
    r.clear()
    n.clear()


