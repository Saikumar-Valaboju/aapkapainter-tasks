s='Mary Army' # Required Input
s=s.upper() # To Ignore Case converting to upper
s=s.split() # splitting into list
s1=s[0] # getting 2 individuals  strings as s1 and s2
s2=s[1]

if sorted(s1) == sorted(s2):  # sorting charcters and checking 
    print('yes')  # printing Required output
else:
    print('No')
