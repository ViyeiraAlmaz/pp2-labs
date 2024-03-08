#ex1
import os
path = 'C:\\Users\\User\\Desktop'
print("Only directories:")
print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([name for name in os.listdir(path)])
print()
#ex2
print('exist:', os.access('c:\\Users\\User\\Desktop\\pp2-labs', os.F_OK))
print('readable:', os.access('c:\\Users\\User\\Desktop\\pp2-labs', os.R_OK))
print('writable:', os.access('c:\\Users\\User\\Desktop\\pp2-labs', os.W_OK))
print('executable:', os.access('c:\\Users\\User\\Dekstop\\pp2-labs', os.X_OK))
print()
#ex3
print("Test a path exists or not:")
path = r'C:\\Users\\User\\Dekstop\\hj'
print(os.path.exists(path))
path = r'C:\\Users\\User\\Desktop\\rw'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))
print()
#ex4
f=open("C:\\Users\\User\\Desktop\\Leorio.txt","r")
counter=0
c=f.read()
clist=c.split("\n")
for i in clist:
    if i:
        counter+=1
print(f"This is the number of lines in the file {counter}")
f.close()
print()
#ex5
alist = ["1", "C2", "J3", "C4","J5", "U6"]
alist2 = ['1s','2s','3s','4s','5s','6s']
f5 = "yoru.txt"
myfile = open(f5,'w')
for i in range(0,6):
    thetext = alist[i] + '-' +alist2[i]+'\n'
    myfile.write(thetext)
myfile.close()
print('The list written written')
print()
#ex6
a=64
for i in range(0,26):
    i+=a+1
    f = open(chr(i)+'.txt','w')
    f.close()
print()
#ex7
with open('yoru.txt','r') as file, open('A.txt','w') as myfile:
    for i in file:
        myfile.write(i)
myfile.close()
myfile = open('A.txt','r')
print(myfile.read())
myfile.close()
print()
#ex8
if os.access("c:\\Users\\User\\Desktop\\koiryu.txt",os.F_OK)==True:
    os.remove("c:\\Users\\User\\Desktop\\koiryu.txt")
else:
    print("file does not exists")