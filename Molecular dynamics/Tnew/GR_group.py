import matplotlib.pyplot as plt
from os import mkdir, path

if not path.exists('properties plot'):
    mkdir('properties plot')

r = []
g = []
nnn = 0
filenum = 12
x = [0,5]
y = [1,1]
plt.figure(figsize=(12,9))
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
    plt.subplot(3,4,i+1)
    plt.plot(r, g, '.-')
    plt.ylim([0,7.5])
    plt.plot(x,y, '--', color='r')
    plt.grid(0.1, linestyle='--')
    plt.title("T"+str(round(nnn,1)) + " g-r relationship plot")
    plt.xlabel('r')
    plt.ylabel('g')
    r.clear()
    g.clear() 
plt.tight_layout()
plt.savefig("properties plot/g-r relationship subplots"+".png")
plt.show()


