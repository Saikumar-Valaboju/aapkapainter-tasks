ar=[1,2,3,2,1] # Required Input
s=set() # creating empty set

for i in range(len(ar)):
    if ar[i] in s: 
        print(ar[i]) # checking the element in set t if available prnting and breaking
        break
    else:
        s.add(ar[i])  # if not there adding to set

# Required output:2
