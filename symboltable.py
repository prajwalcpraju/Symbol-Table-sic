
opcode = ['STA','COMP','LDA','JSUB','LDT','LDX','LDCH','STCH','TIXR','JLT',"RESB","WORD","BYTE","RESW"]
with open("sicfile.txt","r")as file:
    lines = file.readlines()
    #print(count)
    
table=[]
label=[]
for i in lines:
    as_list=i.split(" ")
    table.append(as_list)
#print(table[0][0])

print("Symbol\tLoc")
print(table[0][0],"\t",0)

loc=0

for i in range(1,5):
    if(len(table[i])<=3):    
        if table[i][1] in opcode:
            if len(table[i][0])==0:
                loc=loc+3
                print(" ")
            else :
                if(table[i-1][1]=="RESB"):
                    loc=loc+(int(table[i-1][2]))
                    print(table[i][0],"\t",loc)
                if(table[i-1][1]=="BYTE"):
                    if(table[i-1][2][0]=="C"):
                        loc=loc+(len(table[i-1][2]))-4
                        print(table[i][0],"\t",loc)
                    else:
                       print("invalid")
                if(table[i-1][1]=="RESW"):
                    loc=loc+(int(table[i-1][2]))*3
                    print(table[i][0],"\t",loc)
                if(table[i-1][1]=="WORD"):
                    loc=loc+3
                    print(table[i][0],"\t",loc)
                else:
                    loc=loc+3
                    print(table[i][0],"\t",loc)
        else:
            print("invalid")
    else:
         print("invalid")
            
    
    
        
    
    


#for i in lines:
    #code=i.split(" ") 
    #print(code)
