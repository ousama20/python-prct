while True:
    line= input("<")
    if line[0]=="#":
        continue
    if line=="done":
        break
    print(line)
print("done")

n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1
found=False
z=-1
m=0
total=0
print("befor",z,m,total)
print('K----Z----M-----TOTAL-----FOUND')
for k in [50,-1,70,3,1,98,66]:
    if k==3:
        found=True
    total=total+k
    m=m+1
    if k<z:
        z=k
        
    print(k ,'|', z ,'|', m ,'|', total,'|',found)    
print("the smalest number ",z)
print("the loop has worked ",m,"time")
print("the total after the loop",total)
print("the averge",total/m)