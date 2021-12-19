
from collections import Counter

opcode = ['STA','COMP','LDA','JSUB','LDT','LDX','LDCH','STCH','TIXR','JLT']
declare = ['RESB','RESW','BYTE','WORD']
table=[]
label=[]
with open("sicfile.txt","r")as file:
    lines = file.readlines()
    #print(count)

for i in lines:
    as_list=i.split(" ")
    table.append(as_list)
#print(table[0][0])



for i in range(6):
    label.append(table[i][0])
    #print(label)
    
x=Counter(label)
label_time=max((x.values()))


loc=0

if(label_time==1): 
   print("Symbol\tLoc")
   print(table[0][0],"\t",0)
   for i in range(1,6):
      if(len(table[i])==3):    
          if table[i][1] in opcode:
              if len(table[i][0])==0:
                  loc=loc+3
                  print("")
              else:
                  loc=loc+3
                  print(table[i][0],"\t",loc)
          elif table[i][1] in declare:
              if(table[i-1][1]=="RESB"):
                  loc=loc+(int(table[i-1][2]))
                  print(table[i][0],"\t",loc)
              elif(table[i-1][1]=="BYTE"):
                  if(table[i-1][2][0]=="C"):
                      loc=loc+(len(table[i-1][2]))-4
                      print(table[i][0],"\t",loc)
              elif(table[i-1][1]=="RESW"):
                  loc=loc+(int(table[i-1][2]))*3
                  print(table[i][0],"\t",loc)
              elif(table[i-1][1]=="WORD"):
                  loc=loc+3
                  print(table[i][0],"\t",loc)
              else:
                  loc=loc+3
                  print(table[i][0],"\t",loc)
          else:
               print("invalid line")
            
      elif(len(table[i])==2):
          if table[i][0] in opcode:
              loc=loc+3
              print("")
          else:
              if table[i][1] in opcode:
                  loc=loc+3
                  print(table[i][0],"\t",loc)
      else:
          print("invalid line")
else:
    print("label cannot declare two times")
            
    
    
        
    
    


#for i in lines:
    #code=i.split(" ") 
    #print(code)
