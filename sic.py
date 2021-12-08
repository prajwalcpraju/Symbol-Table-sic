
opcode = ['STA','COMP','LDA','JSUB','LDT','LDX','LDCH','STCH','TIXR','JLT']
declare=["RESB","WORD","BYTE","RESW"]
label=[]  
loc=0
i=0
j=0
k=0
l=0
list=[]
code=[]

print("Enter SIC CODE")
x=input("program name :").split()
n=int(input("Number of instructions:\t"))
p=int(input("Number of declarations:\t"))
for k in range(n):
    b=[]
    for l in range(3):
        b.append((input()))
    code.append(b)
    
print("Enter the memory declaration")
for i in range(p):          
    a =[]
    for j in range(3):     
         a.append((input()))
    list.append(a)
print()

print("The Assembler is")
print(x[0]," ",x[1]," ","0")    
for i in range(n):
    for j in range(3):
        print(code[i][j], end = " ")
    print()
for i in range(p):
    for j in range(3):
        print(list[i][j], end = " ")
    print()
print()

print("Symbol\tLoc")
print(x[0],"\t","0")   
for i in range(n):
    label.append(code[i][0])
    #print(label)
    count=label.count(code[i][0])-label.count("")
    #print(count)
i=0

if(count==1 or count==0):
    if(code[i][0]==code[0][0]):
        loc=0
        print(code[0][0],"\t\t",loc)
    for i in range(1,n):
        if code[i][1] in opcode:
            if len(code[i][0])==0:
                loc=loc+3
                print(" ")
            else:
                loc=loc+3
                print(code[i][0],"\t\t",loc)
else:
    print("invalid")
 
for i in range(p):
    if list[i][1] in declare:
        if(list[i-1][1]=="RESB"):
            loc=loc+(int(list[i-1][2]))
            print(list[i][0],"\t",loc)
        if(list[i-1][1]=="BYTE"):
            if(list[i-1][2][0]=="C"):
                loc=loc+(len(list[i-1][2]))-3
                print(list[i][0],"\t",loc)
            else:
                print("invalid")
        if(list[i-1][1]=="RESW"):
            loc=loc+(int(list[i-1][2]))*3
            print(list[i][0],"\t",loc)
        if(list[i-1][1]=="WORD"):
            loc=loc+3
            print(list[i][0],"\t",loc)
                    

                    
    
