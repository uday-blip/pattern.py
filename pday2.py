# H pattern
fruit=5
mid=fruit//2+1
for row in range(1,fruit+1):
    res=""
    for col in range(1,fruit+1):
        if row==mid or col==1 or col==fruit:
            res+="H"+" "
        else:
            res+=" "+" "
    print(res)
print()
# Z pattern
fruit=5
for row in range(1,fruit+1):
    pat=""
    for col in range(1,fruit+1):
        if  row==1 or row==fruit or row+col==fruit+1:
            pat+="z"+" "
        else:
            pat+=" "+" "
    print(pat)
print()
# N pattern
fruit=5
for row in range(1,fruit+1):
    n=""
    for col in range(1,fruit+1):
        if row==col or col==1 or col==fruit:
            n+="n"+" "
        else:
            n+=" "+" "
    print(n)
print()
# I pattern
fruit=5
mid=fruit//2+1
for row in range(1,fruit+1):
    i=""
    for col in range(1,fruit+1):
        if row==1 or row==fruit or col==mid:
            i+="i"+" "
        else:
            i+=" "+" "
    print(i)

            
