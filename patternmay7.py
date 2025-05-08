#print a pattern of  N
rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        if j==1 or j==rows or i==j :
            pattern+="*"+" "
        else:
            pattern+=" "+" "
    print(pattern)
print()

#print the pattern of Z
rows=5
mid=rows//2+1
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        if i==1 or i==rows or i+j==rows+1:
            pattern+="*"+" "
        else:
            pattern+=" "+" "
    print(pattern)
print()

#print the pattern of a R
rows=5
mid=rows//2+1
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        if i==1 or j==1 or i==mid:
            pattern+="*"+" "
        elif i<mid and j==rows or i>mid and i==j:
            pattern+="*"+" "
        else:
            pattern+=" "+" "
    print(pattern)