l=[1,2,3,2,1] # Required List

p1,p2=0,0 # declaring 2 variables

tmp='pl1' # declare 1 tmp varibale for
for i in range(len(l)):
    if l[i]==1 or l[i]==3:
        if tmp == 'pl1':
            p1+=l[i]
            tmp='pl2'
        else:
            p2+=l[i]
            tmp='pl1'
    else:
        if tmp == 'pl1':
            p1+=l[i]
        else:
            p2+=l[i]
print('p1:',p1,'p2',p2)
