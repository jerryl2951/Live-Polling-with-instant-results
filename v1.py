

name=[]
con=[]
nv=0
n=int(input("Enter the no of contestants:"))
vl=[]
ol=[]
for d in range(0,n):
    vl.append(0)
for d in range(1,n+1):
    con.append(str(d))
for a in range(1,n+1):
    print("Enter name",a)
    nm=input()
    name.append(nm)
voters=int(input("Enter the no of voters:"))
for i in range(1,voters+1):
    print(end="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("   ",i)
    for b in range(0,n):
      print((b+1),"for",name[b])


    v=input("Enter your vote:")
    for c in range(0,n):
     if(v==str(c+1)):
       vl[c]=vl[c]+1

    if v not in con and(v!="STOPPOLL"):
        nv+=1
    if(v=="STOPPOLL"):
        i-=1
        break;
print(end="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
ch=input("Press Y to see the results:")
if(ch=="Y"):
 print(end="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
 f1=open("/home/school/Downloads/voting/results","w")
 print("Election votes percentage   total no of people voted:",i)
 f1.write("total no of people voted:")
 f1.write(str(i))
 f1.write('\n')
 for c in range(0,n):
   print(name[c],"-",vl[c]," percentage:",(vl[c]/i)*100,"%")
   f1.write(name[c])
   f1.write("-")
   f1.write(str(vl[c]))
   f1.write('\n')
 print("no of invalid votes-",nv)
 f1.write("no of invalid votes-")
 f1.write(str(nv))
 f1.close()
 ol=sorted(vl)
 if(ol[-1]==ol[-2]):
     print(" TIE Between ")
     for i in range(0,n):
         if(vl[i]==ol[-1]):
             print(name[i],end="      ")
 else:
  for i in range(0,n):
     if(ol[-1]==vl[i]):
         print(name[i],"won by",ol[-1]-ol[-2],"votes")

else:
    print("Repeat the POLL")