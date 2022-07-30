def runfile(d):    
    f=open(d,'r')
    a=f.readlines()
    global z
    z=[]
    for i in a:
        b=i.split()
        z.append(b)
    f.close
    return z
z=runfile('SalesDataTAB.txt')
print(z)
# ----------------------------------------------------------------/

# z=[["6",4.0],["2","5","hello","8"],["3",'hammad',"3"],["1","2","3"]]
# for i in range(len(l)):
#     l[i]=int(l[i])
# print(l)
    
# ---------------------------------------------------------------/
for r in range(len(z)):
    for c in range(len(z[r])):
        try:
            z[r][c]=int(z[r][c])
        except:
            z[r][c]=z[r][c]    
print(z)        