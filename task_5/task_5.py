

for i in range(32, 127+1):
    print(chr(i), sep='\t', end=('\n' if ((i-1)%10==0 and i!=32) else ' '))