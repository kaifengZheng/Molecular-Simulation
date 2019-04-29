import matplotlib.pyplot as plt
from os import mkdir,path

## The main goal of this program is to draw the plots of coordination numbers over different distances
#                                  *n(r)-r

if not path.exists('properties plot'):
    mkdir('properties plot')


r = []
n = []
T = 0
filenum = 12
plt.figure(figsize=(12,9))
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
    plt.subplot(3,4,i+1)
    plt.plot(r, n, '.-', 'r')
    plt.grid(0.1, linestyle='--')
    plt.title("T"+str(round(T,1)) + " n-r plot")
    plt.xlabel('r')
    plt.ylabel('n')
    plt.xlim([0,2])
    plt.ylim([0,40])
    plt.xticks([0,0.5,1,1.5,2],[0,0.5,1,1.5,2])
    plt.yticks([0,5,10,15,20,25,30,35,40],[0,5,10,15,20,25,30,35,40])
    r.clear()
    n.clear()

plt.tight_layout()
plt.savefig("properties plot/n-r relationship subplots.png")
plt.show()


