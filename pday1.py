# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
fruit=5
for row in range (1,fruit+1):
    num=""
    for col in range(1,row+1):
        num+=str(row)+" "
    print(num)
print()
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5    
fruit=5
for row in range(1,fruit+1):
    p=""
    for col in range(1,row+1):
        p+=str(col)+" "
    print(p)
print()
# 1
# 2 3
# 4 5 6
# 7 8 9 10
fruit=5
c=1
for row in range(1,fruit):
    pat=""
    for col in range(1,row+1):
        pat+=str(c)+" "
        c+=1
    print(pat)